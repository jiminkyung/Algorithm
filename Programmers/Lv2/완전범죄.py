# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/389480


# DFS + 메모이제이션
def solution(info: list[list[int]], n: int, m: int):
    L = len(info)
    memo = {}  # 메모이제이션 안쓰면 통과 X

    def dfs(A: int, B: int, idx: int) -> int:
        nonlocal memo

        # A, B 모두 잡히지 않고 물건을 모두 훔쳤다면, A의 흔적 갯수 반환
        if idx == L:
            return A
        
        # 메모에 이미 저장되어있을경우 해당 값 반환
        if (A, B, idx) in memo:
            return memo[(A, B, idx)]

        min_cnt = n + 1

        # n, m 이상이 되지 않을 경우에만 dfs 진행
        if A + info[idx][0] < n:
            min_cnt = min(min_cnt, dfs(A + info[idx][0], B, idx + 1))
        if B + info[idx][1] < m:
            min_cnt = min(min_cnt, dfs(A, B + info[idx][1], idx + 1))
        
        memo[(A, B, idx)] = min_cnt

        return memo[(A, B, idx)]
    

    cnt = dfs(0, 0, 0)
    return cnt if cnt != n + 1 else -1