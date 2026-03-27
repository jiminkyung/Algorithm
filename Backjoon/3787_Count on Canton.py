# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/3787
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    data = map(int, stdin.read().splitlines())

    for N in data:
        # d번째 대각선까지의 항의 갯수: d * (d+1) // 2, 그리고 항의 갯수를 N이라 치면,
        # d * (d+1) // 2 >= N 이 나옴.
        d = 1
        while d * (d+1) // 2 < N:
            d += 1

        # k: d번째 대각선에서 몇 번째 항인지. N개의 항 - (d-1번째 대각선까지의 항의 갯수) 로 구하면 된다.
        k = N - (d * (d-1) // 2)

        # 짝수번째 대각선의 경우, / 방향임. 분자 증가 + 분모 감소
        # 홀수번째는 반대로 분자 감소 + 분모 증가
        ret = None

        if d % 2 == 0:
            ret = f"{k}/{(d+1) - k}"
        else:
            ret = f"{(d+1) - k}/{k}"
        
        print(f"TERM {N} IS {ret}")


main()


# 또는 근의 공식을 사용해서 풀 수 있음.
from sys import stdin


def main():
    data = map(int, stdin.read().splitlines())

    # d번째 대각선까지의 항의 갯수: d * (d+1) // 2, 그리고 항의 갯수를 N이라 치면,
    # d * (d+1) // 2 >= N 이 나옴. 요걸 근의 공식을 활용하여 풀면, d = ceil(-1 + sqrt(1 + 8N)) / 2 가 나옴.
    for N in data:
        d = int((-1 + (1 + 8*N) ** 0.5) / 2)
        if d * (d + 1) // 2 < N:
            d += 1

        # k: d번째 대각선에서 몇 번째 항인지. N개의 항 - (d-1번째 대각선까지의 항의 갯수) 로 구하면 된다.
        k = N - d * (d - 1) // 2

        # 짝수번째 대각선의 경우, / 방향임. 분자 증가 + 분모 감소
        # 홀수번째는 반대로 분자 감소 + 분모 증가
        ret = None

        if d % 2 == 0:
            ret = f"{k}/{(d+1) - k}"
        else:
            ret = f"{(d+1) - k}/{k}"
        
        print(f"TERM {N} IS {ret}")


main()