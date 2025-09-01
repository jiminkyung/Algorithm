# 수학
# 구현
# 정수론
# 유클리드 호제법


# 문제: https://www.acmicpc.net/problem/2090
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    nums = sorted(map(int, input().split()))

    # 분자: 최소공배수, 분모: N개의 수들 1/A를 최소공배수로 통분한 뒤의 분자값.
    # 수가 1개라면 A/A = 1/1 반환
    if N == 1:
        print(f"{nums[0]}/1")
        return

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    

    # 🗝️1/A들의 최소공배수를 구해야 함.

    # 최소공배수(LCM) 계산
    # => 두 수일 때는 lcm(a,b) = a*b // gcd(a,b)
    # => 여러 수일 때는 → lcm(lcm(a,b), c) 식으로 두 개씩 순차적으로 갱신

    n1 = nums[0]  # 분자
    
    for i in range(1, N):
        n1 = lcm(n1, nums[i])
    
    n2 = 0  # 분모

    for i in range(N):
        n2 += n1 // nums[i]
    
    # 🚨분자, 분모 결과를 최대공약수로 한번 더 나눠줘야함.
    g = gcd(n1, n2)

    print(f"{n1//g}/{n2//g}")


main()