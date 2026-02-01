# 수학
# 구현
# 정수론
# 시뮬레이션
# 비둘기집 원리


# 문제: https://www.acmicpc.net/problem/3189
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    A, B, C = map(int, input().split())

    # A * B^x의 끝 자리수가 C가 되는 최소한의 x를 구해야 함.
    # (C의 길이+1)만큼의 10^x 자릿수만 신경쓰면 되므로, 10^(C의길이)를 MOD로 설정.
    MOD = 10 ** len(str(C))

    curr = A
    # 넉넉하게 B^1 ~ B^MOD 까지 연산
    for i in range(1, MOD+1):
        curr = (curr * B) % MOD

        if curr == C:
            print(i)
            break
    else:
    # 동일한 패턴이 없었다면 불가능한거임.
        print("NIKAD")


main()