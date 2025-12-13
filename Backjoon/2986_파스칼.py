# 수학
# 정수론
# 소수 판정


# 문제: https://www.acmicpc.net/problem/2986

# 1 -> 0, 10 -> 5, 27 -> 18
# i가 N의 약수일때 나머지가 0이 되면서 멈춤.
# counter는 1씩 증가하는 모양임.
# => N의 최대 약수만큼 빼주면 됨.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    ret = [1]  # N = 1일때 0

    # 가장 큰 공약수 구하기
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            ret.append(i)
            ret.append(N // i)
    
    ret.sort()
    print(N - ret[-1])


main()