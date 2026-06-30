# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/154538

# 1) BFS 사용
def solution(x, y, n):
    
    def bfs() -> int:
        visited = set()
        curr = [(x, 0)]
        
        while curr:
            nxt = []
            for num, cnt in curr:
                # 이미 y를 초과했다면 패스
                if num > y:
                    continue
                
                if num == y:
                    return cnt
                
                for new_num in (num + n, num * 2, num * 3):
                    if new_num in visited:
                        continue
                    visited.add(new_num)
                    nxt.append((new_num, cnt + 1))
            curr = nxt[:]
        
        return -1
            
    return bfs()


# 2) DP 사용
def solution(x, y, n):
    INF = float("inf")
    dp = [INF] * (y+1)
    dp[x] = 0
    
    for i in range(x, y+1):
        if dp[i] == INF:
            continue
            
        for nxt in (i + n, i * 2, i * 3):
            if nxt <= y:  # nxt값이 y를 초과하지 않을경우에만 dp 갱신
                dp[nxt] = min(dp[nxt], dp[i] + 1)
            
    return dp[y] if dp[y] != INF else -1