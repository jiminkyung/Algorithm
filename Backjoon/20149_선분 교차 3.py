# 기하 2


# 문제: https://www.acmicpc.net/problem/20149

# 🚨 선분이 완전히 겹치는 경우엔 좌표 출력 X
# 선분 교차 + 좌표 출력 가능으로 인정되는 케이스는 다음과 같다.
    # 1. 선분이 X자 형태로 교차(일반적인 교차)
    # 2. 선분의 끝점이 다른 선분 내에 존재
    # 3. 선분의 한 끝점이 다른 선분의 한 끝점과 겹침

# 참고👉 https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-20149-%EC%84%A0%EB%B6%84-%EA%B5%90%EC%B0%A8-3-Java-Python / https://yiyj1030.tistory.com/508

# 메모리: 31252KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def check():
    ret1 = ccw(p1, p2, q1) * ccw(p1, p2, q2)
    ret2 = ccw(q1, q2, p1) * ccw(q1, q2, p2)
    if ret1 <= 0 and ret2 <= 0:
        # 둘 다 0이라면 기울기가 같다 => 일직선상에 위치
        if ret1 == 0 and ret2 == 0:
            # 만약 선분1의 끝점이 선분2의 시작점보다 크거나 같고, 선분1의 시작점이 선분2의 끝점보다 작거나 같다면 겹치는것임.
            if p2 >= q1 and p1 <= q2:
                return True
            else:
                return False
        return True
    return False

def check_point():
    x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    return x, y

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2 = (x1, y1), (x2, y2)
q1, q2 = (x3, y3), (x4, y4)

# 시작점, 끝점 맞춰주기
if p1 > p2:
    p1, p2 = p2, p1
if q1 > q2:
    q1, q2 = q2, q1

if check():
    print(1)
    try:  # 기울기가 같을경우 zerodivision 에러가 발생할 수 있음.
        x, y = check_point()
        print(x, y)
    except:
        if p1 == q2:  # 선분1의 시작점이 선분2의 끝점과 겹친다면 그곳이 접점.
            print(*p1)
        elif p2 == q1:  # 선분1의 끝점과 선분2의 시작점이 겹친다면 22.
            print(*p2)
else:
    print(0)