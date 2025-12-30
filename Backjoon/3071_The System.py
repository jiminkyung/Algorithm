# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/3071
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        print(solve())
    

def solve():
    n = int(input())

    # n이 0일 경우는 따로 처리
    if n == 0:
        return 0
    
    ret = ""

    while n:
        m = n % 3
        n //= 3

        if m == 0:
            ret = "0" + ret
        elif m == 1:
            ret = "1" + ret
        else:
        # 나머지가 2일 경우, 2 = 3 - 1 이므로 현재 자리값을 -1로 설정하고.
        # 다음 자리값을 +1 증가시키기 위해 n += 1 처리.
            ret = "-" + ret
            n += 1
    
    return ret


main()