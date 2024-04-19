# 명쾌한 답이 떠오르지 않아서 gpt에게 물어봤다.
# 결론은 또다시 점화식. 동적 프로그래밍(DP)가 key였다.

def solution(board):
    # 행과 열의 길이를 구함
    n, m = len(board), len(board[0])
    
    # DP 테이블 초기화: 입력 배열과 동일한 크기로 설정하고, board의 값을 복사
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = board[i][j]
    
    # DP를 이용한 가장 큰 정사각형 변의 길이 계산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    # 가장 큰 정사각형의 한 변의 길이를 찾아서 넓이 계산
    max_side = max(max(row) for row in dp)
    return max_side ** 2

# 입력 예시
board1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board2 = [[0,0,1,1],[1,1,1,1]]

# 결과 출력
print(solution(board1))  # 예상되는 출력: 9
print(solution(board2))  # 예상되는 출력: 4