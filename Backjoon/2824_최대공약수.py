# 수학
# 구현
# 정수론
# 소수 판정


# 문제: https://www.acmicpc.net/problem/2824

# 풀고난 후 확인해보니 소수판정으로 분류되어 있던 문제.
# 너무 간단하긴 했어서 다시 찾아봤더니, 아래처럼 간단하게 풀 수 있는건 Python이었기 때문이고...
# 원래는 A, B의 소인수들을 구한 후, 각 소수의 지수 중 더 작은값을 기준으로 계산한다.
# 🗝️A에서 x의 지수가 e1, B에서 x의 지수가 e2일때 x^min(e1, e2)를 계산하는것임.

# 아래에 위 방식대로 푼 풀이 추가.

# 1) gcd로 단순 계산
# 메모리: 32412KB / 시간: 60ms
from sys import stdin


input = stdin.readline

def main():
    def gcd(a, b) -> int:
        """ a, b의 최대공약수를 구하는 함수 """
        while b:
            a, b = b, a % b
        return a
    

    N = int(input())
    num_n = list(map(int, input().split()))
    M = int(input())
    num_m = list(map(int, input().split()))

    num1 = 1
    num2 = 1

    for num in num_n:
        num1 *= num
    
    for num in num_m:
        num2 *= num

    ret = gcd(num1, num2)
    
    MAX = int(1e9)
    if ret >= MAX:
        print(str(ret)[-9:])
    else:
        print(ret)


main()


# 2) 소수판정 풀이
# 메모리: 32412KB / 시간: 1628ms
from sys import stdin


input = stdin.readline

def main():
    # A, B의 소인수들을 딕셔너리에 저장
    A_factor = {}
    B_factor = {}

    def make_factor(num: int, factor: dict) -> dict:
        x = 2
        while x <= (num ** 0.5) + 1:
            while num % x == 0:
                factor[x] = factor.get(x, 0) + 1
                num //= x
            x += 1
        
        # 최종 num이 1이 아니라면 소수라는 뜻
        if num > 1:
            factor[num] = factor.get(num, 0) + 1
        return factor
    

    MAX = int(1e9)
    N = int(input())
    A = list(map(int, input().split()))

    for a in A:
        A_factor = make_factor(a, A_factor)
    
    M = int(input())
    B = list(map(int, input().split()))

    for b in B:
        B_factor = make_factor(b, B_factor)
    
    # A, B가 공통으로 가지고있는 소수들
    all_factor = set(A_factor.keys()) & set(B_factor.keys())
    ret = 1
    
    for factor in all_factor:
        cnt_A = A_factor[factor]
        cnt_B = B_factor[factor]
        # 더 작은 지수값으로 연산
        ret *= factor ** min(cnt_A, cnt_B)
    
    if ret >= MAX:
        print(str(ret)[-9:])
    else:
        print(ret)


main()