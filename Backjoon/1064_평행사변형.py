# 수학


# 문제: https://www.acmicpc.net/problem/1064
# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    ax, ay, bx, by, cx, cy = map(int, input().split())

    # 1. A, B, C가 일직선상에 위치하는지 확인
    # 벡터 AB, AC 의 외적이 0 이라면 일직선상에 위치하므로 평행사변형 불가.
    AB = (bx - ax, by - ay)
    AC = (cx - ax, cy - ay)
    
    if AB[0]*AC[1] - AB[1]*AC[0] == 0:
        print(-1.0)
        return
    
    # 2. 대각선 조합에 따라 계산하기. 중점이 일치하도록 D 계산 후 총 둘레를 비교한다.
    # AC / BD => A+C = B+D => D = A+C - B
    # AB / CD => A+B = C+D => D = A+B - C
    # AD / BC => A+D = B+C => D = B+C - A
    D1 = (ax + cx - bx, ay + cy - by)
    D2 = (ax + bx - cx, ay + by - cy)
    # D3 = (bx + cx - ax, by + cy - ay)  # D3는 사실상 필요없음
    
    def calc(p1: tuple, p2: tuple, p3: tuple) -> int:
        """ 평행사변형 둘레 계산 """
        l1 = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        l2 = ((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5
        return l1*2 + l2*2
    

    ret1 = calc((ax, ay), (bx, by), D1)
    ret2 = calc((ax, ay), (cx, cy), D2)
    ret3 = calc((ax, ay), (bx, by), (cx, cy))

    MAX = max(ret1, ret2, ret3)
    MIN = min(ret1, ret2, ret3)

    print(MAX - MIN)


main()