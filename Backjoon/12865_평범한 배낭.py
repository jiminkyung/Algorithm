# 동적 계획법 1

# 메모리: 227036KB / 시간: 2908ms
from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

def knapsack():
    # dp[i][j]: i번째 물건까지 고려하고 무게 j일 때의 최대 가치
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            # 현재 물건을 배낭에 넣을 수 있는 경우
            if items[i-1][0] <= j:
                # 현재 물건을 넣는 경우와 넣지 않는 경우 중 최대 가치 선택
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                # 현재 물건을 배낭에 넣을 수 없는 경우, 이전 상태 그대로 유지
                dp[i][j] = dp[i-1][j]
    
    return dp[-1][-1]

print(knapsack())


# 줄이기
# 메모리: 34972KB / 시간: 3544ms => 메모리는 확연히 줄었으나, 시간이 증가함.
from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[K])


# 딕셔너리를 활용한 풀이. 188ms...!
"""
나중을 위한 주석
    - bag(가치: 무게)
    - bag[새 가치] > 새 무게일때, bag[새 가치] = 새 무게로 재할당.

    알고리즘 설명:
    1. 물건들을 무게 기준 내림차순으로 정렬
    2. 가능한 모든 가치-무게 조합을 딕셔너리에 저장
    3. 각 물건에 대해:
        a. 현재 가능한 모든 조합과 새 물건을 결합해 새로운 조합을 만든다.
        b. 새 조합이 기존보다 더 효율적(같은 가치, 더 작은 무게)이면 업데이트.
    4. 최종적으로 가장 큰 가치를 반환

    주의:
    - k를 1 증가시켜 사용한다. 이는 '불가능한 무게'를 나타내기 위함임.
"""
def main():
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                tmp[nv]=nw
        bag.update(tmp)

    print(max(bag.keys()))

main()