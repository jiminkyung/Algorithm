# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1421

# 주어지는 나무의 길이는 중복될 수 있음.
# 리스트로 관리 -> 시간: 164ms

# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    N, C, W = map(int, input().split())
    trees = {}

    # 나무 길이가 중복될 수 있으므로 딕셔너리로 관리
    for _ in range(N):
        tree = int(input())
        trees[tree] = trees.get(tree, 0) + 1

    # 가장 많이 벌 수 있는 돈
    max_money = 0

    # L길이로 잘랐을때의 수입 계산
    # 🚨만약 길이가 L이 안되는 나무 or 수입이 마이너스가 되는 경우는 pass
    for L in range(1, max(trees)+1):
        total = 0
        for tree in trees:
            if tree < L:
                continue
            # (tree // L) - int(tree % L == 0): 나무 길이가 L만큼씩 잘랐을때 딱 떨어진다면 -1
            cost = ((tree // L) - int(tree % L == 0)) * C  # 자른 횟수 * 자르는 비용
            money = (tree // L) * L * W - cost             # 조각의 수 * 길이 * 가격
            total += money * trees[tree] if money >= 0 else 0
            
        max_money = max(max_money, total)
    
    print(max_money)


main()