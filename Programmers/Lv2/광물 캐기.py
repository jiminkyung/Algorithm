# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/172927

# DFS(백트래킹) + 메모이제이션을 사용. 사실 입력값이 적어서 메모이제이션은 안 넣어도 되긴 하다.

def solution(picks: list[int], minerals: list[str]) -> int:
    size = (len(minerals) + 4) // 5  # 사용해야할 곡괭이 수 (가지고있는 곡괭이 수와는 별개임)
    fatigue = [[0, 0, 0] for _ in range(size)]  # fatigue[i][j]: i번째 턴에서 j 곡괭이를 사용했을때의 피로도

    # 광물들을 한 세트당 5개로 쪼갠 후, 세트마다 곡괭이별 피로도 계산.
    for i in range(0, len(minerals), 5):
        for j in range(3):
            for k in range(i, min(len(minerals), i+5)):
                if minerals[k] == "diamond":
                    fatigue[i//5][j] += 5 ** j
                elif minerals[k] == "iron":
                    fatigue[i//5][j] += 5 ** max(j-1, 0)
                else:
                    fatigue[i//5][j] += 5 ** max(j-2, 0)
    
    memo = {}

    def dfs(curr: int, pick: list[int]):
        """
        curr: 현재 캐야할 광물 세트의 인덱스
        pick: 현재 남아있는 곡괭이 수
        memo[(curr, pick)]: 현재 (curr, pick) 상태일때, 앞으로 필요한 최소 피로도 값.
        """
        nonlocal memo

        # 광물을 모두 캤거나, 남아있는 곡괭이가 없다면 0 반환.
        if curr == size or sum(pick) == 0:
            return 0
        
        key = (curr, tuple(pick))

        if key in memo:
            return memo[key]
        
        min_f = int(1e9)

        # 곡괭이별로 DFS(백트래킹) 진행
        for i in range(3):
            if pick[i]:
                pick[i] -= 1
                # 현재상태에서 i번째 곡괭이를 골랐을때의 피로도 값 + 이를 반영한 dfs값이 기존 min_f보다 작으면 갱신.
                min_f = min(min_f, fatigue[curr][i] + dfs(curr+1, pick))
                pick[i] += 1
        
        memo[key] = min_f
        return min_f
    
    return dfs(0, picks)