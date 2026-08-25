# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/87377


def solution(line):
    # 🚨 정답 격자가 1000*1000 이내로 표현된다는 것. 원 격자는 최대 사이즈가 정해지지 않음.
    # -> 격자를 미리 만들어두면 안됨. 주어진 좌표들의 max, min 값을 기준으로 생성해야 함.
    coords = []

    max_x = max_y = float("-inf")
    min_x = min_y = float("inf")

    for i in range(len(line)):
        A, B, E = line[i]
        for j in range(i+1, len(line)):
            C, D, F = line[j]

            if A*D - B*C == 0:
                continue

            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)

            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                coords.append((x, y))
                
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                min_x = min(min_x, x)
                max_x = max(max_x, x)
    
    # 출력에 필요한 배열 생성
    arr = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in coords:
        # 좌표 기준 y == 배열 기준 행 max_y - y
        # 좌표 기준 x == 배열 기준 열 x - min_x
        arr[max_y - y][x - min_x] = "*"
    
    ret = ["".join(line) for line in arr]
    return ret