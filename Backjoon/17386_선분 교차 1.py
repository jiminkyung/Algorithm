# 기하 2


# 문제: https://www.acmicpc.net/problem/17386
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

# ⭐ CCW를 활용하여 선분의 교차 판단 가능.
# P1 = (x1, y1), P2 = (x2, y2) / Q1 = (x3, y3), Q2 = (x4, y4) 라 했을때,
# CCW(P1, P2, Q1) * CCW(P1, P2, Q2)가 음수, CCW(Q1, Q2, P1) * CCW(Q1, Q2, P2)가 음수라면 선분이 교차하는것.
# => Q1, Q2가 선분 P1P2의 양쪽에 위치, P1, P2가 선분 Q1Q2의 양쪽에 위치함을 의미한다.
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2 = (x1, y1), (x2, y2)
q1, q2 = (x3, y3), (x4, y4)

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

print(int(ccw(p1, p2, q1) * ccw(p1, p2, q2) < 0 and ccw(q1, q2, p1) * ccw(q1, q2, p2) < 0))