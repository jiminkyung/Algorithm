# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/60061


# 구현 연습하기 좋은 문제
def solution(n: int, build_frame: list[list[int]]) -> list[list[int]]:
    # 0은 기둥, 1은 보
    arr = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

    # a: 0은 기둥, 1은 보
    # b: 0은 삭제, 1은 설치
    # 문제 조건은 아래와 같음
    # - 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    # - 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

    def check(x, y, a, b) -> bool:
        """
        a: 0은 기둥, 1은 보
        b: 0은 삭제, 1은 추가

        삭제(b=0)의 경우, 인자로 들어온 (x, y)는 삭제하려는 곳 주변의 구조물임.
        따라서 (x, y)에 별다른 구조물이 없다면 삭제에 영향을 받지 않는다는 의미이므로 바로 True 반환.
        """
        if b == 0 and arr[x][y][a] == 0:
            return True
        
        # 기둥 일경우, 바닥에 위치했는지 / 아래에 기둥이 있는지 / 보 위에 위치해있는지 확인.
        if a == 0:
            if y == 0 or (y > 0 and arr[x][y-1][0]) or ((x > 0 and arr[x-1][y][1]) or arr[x][y][1]):
                return True
        # 보 일경우, 왼쪽·오른쪽 아래에 기둥이 위치했는지 / 양 옆으로 보가 존재하는지 확인.
        else:
            if (y > 0 and arr[x][y-1][0]) or (y > 0 and x < n and arr[x+1][y-1][0]) or (0 < x < n and arr[x-1][y][1] and arr[x+1][y][1]):
                return True
        return False


    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            arr[x][y][a] = 0
            flag = True  # 삭제 가능한지 여러 조건을 확인하면서 갱신

            if a == 0:
                # 기둥을 삭제할경우, 위 기둥 / 위 왼쪽·오른쪽 보 검사
                if y < n:
                    flag &= check(x, y+1, 0, 0)  # 위 기둥
                    flag &= check(x, y+1, 1, 0)  # 기둥 꼭대기 기준 오른쪽 보
                    if x > 0:
                        flag &= check(x-1, y+1, 1, 0)  # 기둥 꼭대기 기준 왼쪽 보
            else:
                # 보를 삭제할경우, 위 왼쪽·오른쪽 기둥 / 왼쪽·오른쪽 양 옆 보 검사
                flag &= check(x, y, 0, 0)  # 위 왼쪽 기둥

                if x < n:
                    flag &= check(x+1, y, 0, 0)  # 위 오른쪽 기둥
                
                # 양 옆 보
                if x > 0:
                    flag &= check(x-1, y, 1, 0)
                if x < n:
                    flag &= check(x+1, y, 1, 0)
            
            # 삭제 조건에 부합하지 않는다면 되돌리기
            if not flag:
                arr[x][y][a] = 1
        else:
            if check(x, y, a, 1):
                arr[x][y][a] = 1
    
    ret = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if arr[i][j][k]:
                    ret.append([i, j, k])
    
    return ret