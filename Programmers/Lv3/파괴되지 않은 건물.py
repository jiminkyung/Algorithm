# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/92344


# 2차원 차분 배열 + 누적합
# 누적합 연습 시 다시 풀어볼만한 문제
def solution(board: list[list[int]], skill: list[list[int]]) -> int:
    N, M = len(board), len(board[0])

    # 🗝️ 2차원 차분 배열 + 누적합 을 사용해야 시간초과 없이 통과 가능
    # 직사각형의 네 모서리에만 변화량을 기록하고, 마지막에 2차원 누적합으로 각 칸의 변화량 체크

    # diff[i][j]: (i, j) 좌표의 변화량
    # r2+1, c2+1이 N, M 이 될 수 있으므로 N+1, M+1 크기로 생성
    diff = [[0] * (M+1) for _ in range(N+1)]

    # 1. 각 변화량을 차분 배열에 기록
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        
        # 시작점(r1, c1)에 변화량 전달,
        # 직사각형의 오른쪽(r1, c2+1)과 아래쪽(r2+1, c1) 경계에 취소값,
        # 오른쪽 아래 모서리(r2+1, c2+1)에는 두 번 취소된 값을 복구시키기 위한 값.
        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree
    
    # 2. 2차원 누적합으로 각 칸의 전체 변화량을 복원
    # 위쪽, 왼쪽의 누적값을 더하고 두 번 더해진 왼쪽 위의 값을 빼주는 방식.
    for i in range(N):
        for j in range(M):
            if i > 0:
                diff[i][j] += diff[i-1][j]
            
            if j > 0:
                diff[i][j] += diff[i][j-1]
            
            if i > 0 and j > 0:
                diff[i][j] -= diff[i-1][j-1]
    
    # 3. 원본 board와 변화량 diff를 계산하여 최종 내구도가 1 이상인 건물 카운팅
    cnt = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] + diff[i][j] > 0:
                cnt += 1
    
    return cnt