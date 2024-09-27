# 기하 2


# 문제: https://www.acmicpc.net/problem/1069
# 메모리: 31252KB / 시간: 40ms
from sys import stdin


"""
1. 거리가 D보다 클 경우
: 걷기, 점프 후 걷기, 점프 + 꺾은점프
- jump = distance // D 라 했을때,
- jump-1번 점프 후 남은 거리가 2D 미만이라면, 꺾어서 점프 할 수 있음.
    c² = a² + b² - 2ab cos C 식을 이용해서,
    x² = D² + D² - 2D² cos θ
    = 2D² - 2D² cos θ
    = 2D² (1 - cos θ)
    cos의 범위는 -1 <= cos <= 1 이므로, 위 식을 적용하면 0 ≤ 1 - cos θ ≤ 2 가 된다.
    0 ≤ x² ≤ 4D²  (x² = 2D² (1 - cos θ)이므로 대입) => 0 <= x <= 2D
- 따라서 jump번 점프 후 한번 더 점프한 뒤 되돌아가는 경우는 고려하지 않아도 됨.
- (T * (jump+1) + 되돌아가는거리)가 되므로 3번 경우에서 플러스만 될 뿐임.

2. 거리가 D보다 작은 경우
: 걷기, 점프 후 걷기(-), 두번 꺾은점프
- jump를 따로 구하지 않는다.
- 점프를 하는 경우는 한번 점프 후 되돌아걷거나, 꺾어서 두번 점프하거나. 무조건 둘 중 하나이기 때문임.
"""
input = stdin.readline

X, Y, D, T = map(int, input().split())
distance = (X**2 + Y**2) ** 0.5

if distance >= D:
    # 점프 횟수
    jump = distance // D
    # 1) 걷기, 2) 점프 후 걷기, 3) jump-1번 점프 후 꺾어서 점프 두번하기
    ret = min(distance, T * jump + distance % D, T * (jump + 1))
else:
    # 1) 걷기, 2) 점프 후 되돌아걷기, 3) 꺾어서 점프 두번하기
    ret = min(distance, T + (D - distance), 2 * T)

print(ret)