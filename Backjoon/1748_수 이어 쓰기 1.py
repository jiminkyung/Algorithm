# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/1748
# 메모리: 32412KB / 시간:32ms
from sys import stdin


input = stdin.readline

def main():
    N = input().rstrip()
    N_length = len(N)

    length = 0
    l = 1

    # N의 자릿수-1 까지의 총 길이수 계산. ex) N = 1234일때 999까지의 길이
    while l < N_length:
        # 1~9 = 9, 10~99: 90... 매 반복마다 9 * 10**(자릿수-1)의 값을 더해줌.
        # 9 * 10**0 = 9*1 = 9
        # 9 * 10**1 = 9*10 = 90
        length += (9 * (10 ** (l - 1))) * l
        l += 1
    
    # while문 이후 l == N_length가 됨.
    # 그럼? N이 1253라면, 1253 - 999 가 네자리 숫자의 갯수가 됨.
    # 999를 직접 만들던지, 아님 1000-1 처리를 해주던지... 1000-1이 더 쉬울듯? 10 ** 3 = 1000 이니까,
    # 10 ** (N_length-1) 해준다음 -1 해주면 될듯.
    rest = int(N) - (10 ** (N_length-1) - 1)
    length += N_length * rest
    print(length)


main()