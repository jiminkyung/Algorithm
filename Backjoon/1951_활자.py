# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/1951

# 1) 처음 접근했던 방법
# -> 각 자리마다 필요한 갯수 체크
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline
MOD = 1234567

def main():
    N = input().rstrip()
    L = len(N)

    ret = 0

    # 각 자리에 몇개가 필요한지 계산
    """
    ex) 5551

    i = 0 (5)
    - N[:i+1] = 5
        - 1000 ~ 4999까지 필요한 천의 자리의 갯수는 4000개
    - N[i+1:] = 551
        - 5000 ~ 5551까지 필요한 천의 자리의 갯수는 552개
    
    i = 1 (5)
    - N[:i+1] = 55
        - 100 ~ 5499까지 필요한 백의 자리의 갯수는 5400개
    - N[i+1:] = 51
        - 5500 ~ 5551까지 필요한 백의 자리의 갯수는 52개
    
    i = 2 (5)
    - N[:i+1] = 555
        - 10 ~ 5549까지 필요한 십의 자리의 갯수는 5540개
    - N[i+1:] = 1
        - 5550 ~ 5551까지 필요한 십의 자리의 갯수는 2개
    
    i = 3 (1)
    - N[:i+1] = 5551
        - 1 ~ 5550까지 필요한 일의 자리의 갯수는 5550개
    - N[i+1:] = None

    실제로 필요한 일의 자리의 갯수는 5551개임.
    따라서 마지막에 +1 한 값을 출력해야 함.
    """
    for i in range(L):
        prev = N[:i+1]
        nxt = N[i+1:]

        size = 10 ** (L-i-1)

        if prev:
            prev = int(prev)
            ret += (prev - 1) * size

        if nxt:
            nxt = int(nxt)
            ret += nxt + 1
        
        ret %= MOD
    
    print(ret + 1)


main()


# 2) 훨씬 간단한 방법
# -> 자릿수별로 묶어서 계산하기.
# ex) 149 => 1
    # 1~9 -> 9개, 각 숫자는 1자리 -> 총 9*1개
    # 10~99 -> 90개, 각 숫자는 2자리 -> 총 90*2개
    # 100~149 -> 49개, 각 숫자는 3자리 -> 총 49*3개
    # => 합산하면 끝
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline
MOD = 1234567

def main():
    N = input().rstrip()
    L = len(N)
    ret = 0

    # 551이라면 9 * 1 + 90 * 2...
    for i in range(L-1):
        size = 10 ** i
        ret += 9 * size * (i+1)
        ret %= MOD
    
    # L의 자리 계산
    rest = int(N) - (10 ** (L-1)) + 1
    ret += rest * L
    ret %= MOD

    print(ret)


main()