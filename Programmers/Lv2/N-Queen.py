# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12952

def solution(n):
    # 모든 퀸은 각각 한 행, 한 열을 담당함. 즉 한 행/열 에는 하나의 퀸만 존재할 수 있음.
    cols = set()
    ld = set()  # 왼쪽 대각선 행렬
    rd = set()  # 오른쪽 대각선 행렬

    def dfs(row: int) -> int:
        # 모든 행에 퀸이 존재한다면 1 반환.
        if row == n:
            return 1
        
        cnt = 0  # 아직 배치되지 않은 나머지 퀸들을 배치하는 경우의 수

        for col in range(n):
            # 같은 열에 퀸이 있다면 불가능함
            if col in cols:
                continue

            # 왼/오 대각선 중 하나라도 겹치면 불가능
            # \ 대각선 - (x, y)일때 같은 대각선 행렬에 위치해있다면 x - y값이 같음.
            # ex) (1, 1), (2, 2), (3, 3)...
            if row - col in ld:
                continue

            # / 대각선 - (x, y)일때 같은 대각선 행렬에 위치해있다면 x + y값이 같음.
            # ex) (1, 3), (2, 2), (3, 1)...
            if row + col in rd:
                continue

            # 퀸 배치
            cols.add(col)
            ld.add(row - col)
            rd.add(row + col)

            cnt += dfs(row + 1)

            # 배치한 퀸 제거
            cols.remove(col)
            ld.remove(row - col)
            rd.remove(row + col)
        
        return cnt
    

    return dfs(0)