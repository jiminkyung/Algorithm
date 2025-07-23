# 그래프 이론
# 분리 집합


# 문제: https://www.acmicpc.net/problem/1778
# 메모리: 35800KB / 시간: 520ms
from sys import stdin


input = stdin.readline

def main():
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a, b = find(a), find(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    turn = 1

    while True:
        n, m = map(int, input().split())

        if n == 0 and m == 0:
            break

        # 주어진 쌍들을 유니온 파인드로 합쳐줌
        parent = list(range(n+1))

        for _ in range(m):
            i, j = map(int, input().split())
            union(i, j)
        
        # 총 집합 수
        parents = [find(x) for x in range(1, n+1)]
        print(f"Case {turn}: {len(set(parents))}")

        turn += 1


main()