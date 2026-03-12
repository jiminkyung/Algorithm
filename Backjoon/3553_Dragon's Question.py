# 수학
# 애드 훅


# 문제: https://www.acmicpc.net/problem/3553

# 수식으로 간단하게 풀 수 있는 문제. 애드 훅으로 분류되어있음.

# 1) 피지컬로 통과
# 메모리: 32412KB / 시간: 1384ms
from sys import stdin


input = stdin.readline

def main():
    n, d = map(int, input().split())

    # n자리 범위: 10^(n-1) ~ 10^n-1 임.
    # 근데? 시작값 s와 s+d-1 사이에는 d로 나누어 떨어지는 수가 무조건 있을것이다.
    for num in range(10 ** (n-1), min(10 ** n, 10 ** (n-1) + d)):
        if num % d == 0:
            print(num)
            break
    else:
        print("No solution")
    
    # 🗝️그냥 수식으로 한번에 구하는 방법이 있었다.
    # 범위 시작값 10^(n-1)을 start라고 치면,
    # ceil(start / d) = start 이상의 d의 배수가 d의 배수 중 몇번째 배수인지.
    # 그리고 이 값에 다시 d를 곱해주면? start 이상의 d의 배수 중 가장 최소값을 구할 수 있음.
    # => 만약 이 값이 끝값 10^n-1 보다 크다면 불가능한것.


main()


# 2) 초간단 판별법
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    n, d = map(int, input().split())

    start, end = 10 ** (n-1), 10 ** n - 1
    q = (start + d - 1) // d  # ceil대신 (d-1)을 더해주고 //로 나눠줌.
    num = q * d

    print(num if num <= end else "No solution")


main()