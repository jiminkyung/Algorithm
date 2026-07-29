# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/340198

# 도움이 됐던 반례: https://school.programmers.co.kr/questions/82889
# [1, 2], [["A", "-1"], ["A", "-1"]] -> 답: 1
def solution(mats: list[int], park: list[list[str]]) -> int:
    mats.sort(reverse=True)
    N, M = len(park), len(park[0])
    
    def check(x, y):
        # 작은 사이즈부터 순서대로 확인
        for size in mats:
            # 🚨 >= N, >= M 으로 하면 X
            if x+size > N or y+size > M:
                continue
            
            flag = False
            
            # 사이즈만큼 탐색
            for i in range(x, x+size):
                for j in range(y, y+size):
                    if park[i][j] != "-1":
                        flag = True
                        break
                
                if flag:
                    break
            
            if not flag:
                return size
        return -1
                        
    
    max_size = -1
    
    for i in range(N):
        for j in range(M):
            if park[i][j] == "-1":
                max_size = max(check(i, j), max_size)
    
    return max_size