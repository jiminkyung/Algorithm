# 구현
# 기하학
# 피타고라스 정리


# 문제: https://www.acmicpc.net/problem/1925
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    x = []
    y = []

    for _ in range(3):
        p, q = map(int, input().split())
        x.append(p)
        y.append(q)

    def check(x: list[int], y: list[int]) -> str:
        # 1. 외적으로 일직선상에 위치했는지 체크
        AB = (x[1] - x[0], y[1] - y[0])
        AC = (x[2] - x[0], y[2] - y[0])

        if AB[0]*AC[1] - AC[0]*AB[1] == 0:
            return "X"
        
        # 2. 세 변을 참고해서 예각/직각/둔각 체크 (피타고라스 정리)
        AB = (x[1] - x[0])**2 + (y[1] - y[0])**2
        AC = (x[2] - x[0])**2 + (y[2] - y[0])**2
        BC = (x[2] - x[1])**2 + (y[2] - y[1])**2
        sides = [AB, AC, BC]
        a, b, c = sorted(sides)  # 변의 길이에 따라 정렬

        angle = None

        # 가장 긴 변(c)를 기준으로 각도 계산
        if a + b == c:
            angle = "Jikkak"
        elif a + b > c:
            angle = "Yeahkak"
        else:
            angle = "Dunkak"
        
        # 변의 길이가 같은 갯수에 따라 정, 이등변, 그냥 삼각형으로 분류
        if a == b == c:
            return "JungTriangle"
        elif a == b or b == c or a == c:
            return f"{angle}2Triangle"
        else:
            return f"{angle}Triangle"
    

    print(check(x, y))


main()