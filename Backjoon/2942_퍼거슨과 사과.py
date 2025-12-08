# 수학
# 정수론
# 유클리드 호제법


# 문제: https://www.acmicpc.net/problem/2942
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    R, G = map(int, input().split())
    # 사과의 약수 x = 선수 x명에게 R//x, G//x만큼 줄 수 있음.
    # 🗝️ R, G의 최대공약수를 구한 다음 그 수의 약수를 모두 구하면 됨.
    # 어떤 수 A, B의 최대공약수의 약수 = A, B의 모든 약수

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    

    # 사과의 최대공약수
    g = gcd(R, G)
    
    nums = []
    # 제곱근까지만 순회
    for i in range(1, int(g ** 0.5) + 1):
        # 만약 i로 나누어 떨어진다면, i 저장.
        if g % i == 0:
            nums.append(i)
            # g//i의 값이 i가 아니라면 g//i도 저장.
            if i != (g // i):
                nums.append(g // i)
    
    nums.sort()

    for num in nums:
        print(num, R//num, G//num)


main()