# 기하 2


# 문제: https://www.acmicpc.net/problem/17387

# 17386_선분 교차 1 문제와 유사하나, 끝점이 다른 선분에 포함되어도 교차하는것으로 간주한다.
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2 = (x1, y1), (x2, y2)
q1, q2 = (x3, y3), (x4, y4)

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def is_between(a, b, c):
    return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))

ret1 = ccw(p1, p2, q1) * ccw(p1, p2, q2)
ret2 = ccw(q1, q2, p1) * ccw(q1, q2, p2)

if ret1 == 0 and ret2 == 0:
    # 두 선분이 일직선상에 위치하는 경우엔, 끝점이 다른 선분 위에 위치하는지 체크한다.
    # 하나라도 존재한다면 True, 아니라면 접점이 아예 없다는 뜻이므로 False.
    if is_between(p1, p2, q1) or is_between(p1, p2, q2) or is_between(q1, q2, p1) or is_between(q1, q2, p2):
        print(1)
    else:
        print(0)
else:
    # 그 외엔 끝점이 다른 선분 위에 위치하거나, 아예 교차하는 경우가 된다.
    print(int(ret1 <= 0 and ret2 <= 0))