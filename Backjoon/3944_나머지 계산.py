# 수학
# 정수론


# 문제: https://www.acmicpc.net/problem/3944
# 메모리: 52916KB / 시간: 2428ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    # 모듈러 연산을 활용해야 함.
    # 🗝️ B % (B-1) = 1 이므로, B ≡ 1 (mod B-1) 이 성립됨.
    # 모듈러 식 특성상 A^2 ≡ B^2 이니까,
    # D = n1*B^0 + n2*B^1...에 B^k ≡ 1^k (mod B-1)를 적용하면, 각 자릿수 nk * 1 ... mod B-1로 풀 수 있음.
    # 즉, D의 각 자릿수의 합을 B-1로 나눈 값 == D를 10진수로 변환 후 B-1로 나눈 값 이 되는셈.
    for _ in range(T):
        B, D = input().rstrip().split()
        B = int(B)

        D = sum(map(int, D))
        print(D % (B-1))


main()