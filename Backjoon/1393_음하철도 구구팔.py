# 수학
# 정수론
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1393

# 벡터 정사영(정류장에서 기차 선로로 수선의 발을 내림)을 사용하는 방식도 가능하다.

# 1) 최대공약수, 브루트포스 사용 풀이
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    sx, sy = map(int, input().split())
    ex, ey, dx, dy = map(int, input().split())

    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        return a
    

    # 🗝️최대공약수로 (dx, dy)를 나눠줌.
    # => 열차가 실제로 지나가는 모든 정수 좌표를 체크할 수 있음.
    g = gcd(dx, dy)
    dx //= g
    dy //= g

    time = 0
    min_dist = (sx - ex)**2 + (sy - ey)**2  # 최소거리값을 t=0일때로 초기화

    # 만약 초기 좌표가 -100, 정류장의 위치가 100, 이동거리가 1일경우의 최대 t는 200
    # 따라서 200*최대공약수 + 1을 마지노선으로 설정
    for t in range(1, 200*g + 1):
        nx = ex + t*dx
        ny = ey + t*dy
        dist = (sx - nx)**2 + (sy - ny)**2

        if min_dist <= dist:
            break

        min_dist = dist
        time = t
    
    print(ex + dx*time, ey + dy*time)


main()


# 2) 수선의 발 사용 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    sx, sy = map(int, input().split())
    ex, ey, dx, dy = map(int, input().split())

    # A: (정류장 -> 기차시작점) 벡터
    # D: (기차 진행방향) 벡터
    # => A * D(내적) / D^2

    ax, ay = sx - ex, sy - ey  # A 벡터
    
    top = ax*dx + ay*dy
    bottom = dx**2 + dy**2

    t = top / bottom

    if t < 0:
        x, y = ex, ey
    else:
        x = ex + t*dx
        y = ey + t*dy
    
    print(int(x), int(y))


main()