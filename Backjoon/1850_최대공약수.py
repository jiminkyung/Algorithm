# 수학
# 정수론
# 유클리드 호제법


# 문제: https://www.acmicpc.net/problem/1850

# 메모리: 42176KB / 시간: 44ms
"""
얼떨결에 푼 문제...

🗝️A와 B 자체로 최대공약수를 구함. 해당 값만큼 1을 출력하면 답이 된다.

즉, R(2) = 11, R(5) = 11111... 인 R(x)가 있다고 했을때,
gcd(R(A), R(B)) = R(gcd(A, B)) 인 셈!
=> "1의 개수"와 "실제 수"가 같은 약수 관계를 갖기 때문임.
"""
from sys import stdin


input = stdin.readline

def main():
    A, B = map(int, input().split())

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    print("1" * gcd(A, B))


main()