# 그래프 이론
# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1679

# 본래 BFS의 목적은 최단거리(최단비용)이지만... 이 문제의 경우,
# 퍼져나가며 탐색해야하므로 BFS를 선택한것뿐임.
# + DP로도 풀 수 있는듯. DP 풀이가 더 빠름.

# 메모리: 34952KB / 시간: 52ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    def bfs(nums: list, K: int) -> list:
        ret = set()      # 만들 수 있는 숫자들
        visited = set()  # 사용한 (숫자, 횟수) 저장
        visited.add((0, 0))
        queue = deque([(0, 0)])

        while queue:
            s, cnt = queue.popleft()

            # K번 사용했다면 pass
            if cnt == K:
                continue

            for num in nums:
                if (s+num, cnt+1) not in visited:
                    visited.add((s+num, cnt+1))
                    queue.append((s+num, cnt+1))
                    ret.add(s+num)
        
        return sorted(ret)
    

    ret = bfs(nums, K)
    # 만약 max가 다른값인데, 14까지 만들 수 있다면? => i=15
    # max도 14, 가능한값도 14라면 => i=14
    for i in range(1, max(ret)+1):
        if ret[i-1] != i:
            break
        else:
            i += 1
    
    name = "jjaksoon" if i % 2 != 0 else "holsoon"
    print(f"{name} win at {i}")


main()


# DP 풀이 로직은 아래와 같음.
# 메모리: 32412KB / 시간: 32ms
"""
- dp[x]: x를 만들 수 있으면 True, 없으면 False
- min_cnt[x]: x를 만들 때 사용한 최소 정수 개수
    - dp[0] = True (0은 아무것도 사용하지 않고 만들 수 있음), min_cnt[0] = 0으로 초기화.

- 1부터 차례로 target을 증가시키며 dp, min_cnt 체크.
    - 주어진 정수들을 활용해 target - num을 만들 수 있고,
    - 그때까지 사용한 정수 개수 + 1 이 최대 사용 횟수 K 이하면,
    - target을 만들 수 있다고 판단하고 dp와 min_cnt를 갱신한다.
- 매 target마다 누가 이기는지 확인.
    - 만들 수 없는 경우 (dp[target]이 False)일때,
        - target이 홀수면 짝순이가 승리.
        - target이 짝수면 홀순이가 승리.
"""
from sys import stdin


def dynamic():
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    MAX = max(nums) * K + 2
    dp = [False] * (MAX)
    min_cnt = [int(1e9)] * (MAX)
    dp[0] = True
    min_cnt[0] = 0

    for target in range(1, MAX):
        for num in nums:
            if target - num >= 0 and dp[target - num]:
                if min_cnt[target - num] + 1 <= K:
                    dp[target] = True
                    min_cnt[target] = min(min_cnt[target], min_cnt[target - num] + 1)

        # 매 수마다 누가 이기는지 확인
        if not dp[target]:
            if target % 2 == 1:
                print(f"jjaksoon win at {target}")
            else:
                print(f"holsoon win at {target}")
            return


dynamic()