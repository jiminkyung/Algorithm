# 브루트포스 알고리즘
# 비트마스킹
# 백트래킹


# 문제: https://www.acmicpc.net/problem/2961

# 기본적인 비트마스킹, 메모이제이션 문제인듯.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    memo = {}  # memo[x]: x 조합으로부터 만들 수 있는 조합 중 가장 최소값

    # 신맛, 쓴맛을 따로 저장
    ing = [tuple(map(int, input().split())) for _ in range(N)]
    S, B = map(list, zip(*ing))

    def dfs(curr: int, s: int, b: int) -> int:
        if curr in memo:
            return memo[curr]
        
        # 차이 계산
        min_diff = abs(s - b)

        # 현재 조합에 새로운 재료 추가
        for i in range(N):
            if curr & (1 << i):  # 이미 선택한 재료라면 pass
                continue

            # 새롭게 만든 조합과 기존 조합 중 차이가 더 적은 값으로 갱신
            min_diff = min(min_diff, dfs(curr | (1 << i), s * S[i], b + B[i]))
        
        # memo에 저장 후 return
        memo[curr] = min_diff
        return min_diff
    

    ret = float("inf")

    # 각 재료를 첫번째로 넣어보기
    for i in range(N):
        ret = min(ret, dfs(1 << i, S[i], B[i]))
    
    print(ret)


main()