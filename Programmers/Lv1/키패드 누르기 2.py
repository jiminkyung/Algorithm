# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers: list[int], hand: str) -> str:
    arr = [[i, i+1, i+2] for i in range(1, 8, 3)] + [["*", 0, "#"]]
    dist = {arr[i][j]: (i, j) for i in range(4) for j in range(3)}  # 키 - 위치 맵핑
    l, r = "*", "#"
    ret = ""
    
    for num in numbers:
        if num in (1, 4, 7):
            ret += "L"
            l = num
        elif num in (3, 6, 9):
            ret += "R"
            r = num
        else:
            x, y = dist[num]
            lx, ly = dist[l]
            rx, ry = dist[r]
            l_dist = abs(lx - x) + abs(ly - y)
            r_dist = abs(rx - x) + abs(ry - y)
            
            # 1. 왼쪽
            if l_dist < r_dist:
                ret += "L"
                l = num
            # 2. 오른쪽
            elif l_dist > r_dist:
                ret += "R"
                r = num
            # 3. 같을경우, 어느손잡이인지에 따라 결정
            else:
                if hand == "left":
                    ret += "L"
                    l = num
                else:
                    ret += "R"
                    r = num
            
    return ret