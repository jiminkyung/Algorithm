"""
피로도를 사용하여 던전을 탐험하고, 최대한 많은 던전을 탐험할 수 있는 경우의 수를 찾는 문제.
k: 현재 피로도
dungeons: 던전 정보를 담은 2차원 배열 ([[최소 필요 피로도, 소모 피로도], ...])

백트래킹(Backtracking):
- 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾는 기법
- 모든 경우의 수를 탐색하면서, 제약 조건을 만족하는 해를 찾는 알고리즘
- 불필요한 경우의 수를 줄이면서 최적의 해를 찾을 수 있음

동작 과정:
1. 던전 탐험의 모든 경우의 수를 탐색하기 위해 백트래킹 사용
2. 현재 상태에서 탐험 가능한 던전을 선택하고, 던전 탐험 후 다음 던전 탐색
3. 탐험할 수 있는 던전이 없으면 이전 상태로 돌아가서(백트래킹) 다른 경우의 수 탐색
4. 모든 경우의 수를 탐색하면서 최대 던전 탐험 수를 갱신
5. 최종적으로 최대 던전 탐험 수를 반환
"""

def solution(k: int, dungeons: list) -> int:
    n = len(dungeons)
    ret = 0

    def backtrack(k, visited, count):
        nonlocal ret
        ret = max(ret, count)

        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                backtrack(k-dungeons[i][1], visited, count+1)
                visited[i] = False
    
    visited = [False] * n
    backtrack(k, visited, 0)

    return ret