# 수학


# 문제: https://www.acmicpc.net/problem/1500
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    S, K = map(int, input().split())

    # K개의 수들을 최대한 비슷하게 만들어야 곱이 커짐.
    # a = S // K, b = S % K 라고 할때,
    # K개중 b개는 a+1로, (K-b)개는 a로 설정하면 최대한 비슷하게 맞춰짐.

    a = S // K
    b = S % K

    # 나머지만큼의 숫자를 a+1로, 그 외에는 a로 설정.
    ret = ((a + 1) ** b) * (a ** (K - b))
    print(ret)


main()