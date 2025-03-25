# 비트마스킹


# 문제: https://www.acmicpc.net/problem/1052

# 동일한 양의 물병끼리만 합칠 수 있음.
# => 2진수를 활용하면 쉽게 풀 수 있음!

# N을 2진수로 변환 후 1의 갯수가 K 이하라면 통과.
# 아니라면, 될때까지 N에 1씩 더해준다.
# ex) 11(3) + 1 => 100(4)

# 메모리: 32412KB / 시간: 1768ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    cnt = 0

    while bin(N).count("1") > K:
        N += 1
        cnt += 1
    
    print(cnt)


main()