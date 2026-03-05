# 구현


# 문제: https://www.acmicpc.net/problem/3496

# 실제로 정보 압축 시 사용된다고 함. (Truncated Binary Coding)
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    m = int(input())

    n = 1
    while 2 ** n < m:
        n += 1
    
    # m <= 2^n 이어야 함.
    # 2^n - m = k 일때, 이 k는 n-1개의 비트로 구성해도 괜찮은 갯수가 된다.
    # 만약 k = 2라고 한다면...
    # 00 01 이 될것이고, 접두사 규칙에 따라 000 001 / 010 011 은 사용할 수 없게 됨.
    # 즉, n-1개 비트 하나당 n개 비트 2개를 잡아먹는 셈. (이진트리를 생각해보라)
    
    # 따라서 나머지 m-k개의 경우는 2k 이상부터 가능.
    # -> k개의 수는 n-1 비트로 치환하고, 나머지는 (숫자 + k)를 n 비트로 치환하면 된다.
    k = 2 ** n - m
    ret = []
    
    for i in range(k):
        ret.append(f"{bin(i)[2:].zfill(n-1)}")
    
    for i in range(k, m):
        ret.append(f"{bin(i + k)[2:].zfill(n)}")
    
    print(*ret, sep="\n")


main()