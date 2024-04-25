def solution(balls, share):
    n1, n2, n3 = 1, 1, 1

    for i in range(balls, 0, -1):
        n1 *= i

    for i in range((balls-share), 0, -1):
        n2 *= i

    for i in range(share, 0, -1):
        n3 *= i

    return n1 // (n2 * n3)

# 정말 무식하게 풀었다. 다시는 이렇게 풀고싶지 않다!

# 다른분의 풀이 1
def solution(balls, share):
    a, b = 1, 1
    for i in range(1,share+1):
        a *= balls
        balls -= 1
        b *= i
    return int(a / b)

# 다른분의 풀이 2 - 와우......
import math


def solution(balls, share):
    return math.comb(balls, share)