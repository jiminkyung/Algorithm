# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42861


def solution(n: int, costs: list[list[int]]) -> int:
    # 크루스칼을 써보자.
    costs.sort(key=lambda x: x[2])
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    

    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            return True
        return False
    

    cost = 0

    for u, v, w in costs:
        if union(u, v):
            cost += w
    
    return cost