# 수학


# 문제: https://www.acmicpc.net/problem/2097
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    """
    🗝️정사각형에 가까운 모양일수록 둘레가 작아짐.

    길이 1은 점 두개가 이어진 선분. 즉 9개의 점으로 3x3 배열을 만들면, 실질적인 직사각형의 둘레는 2x2 = 4인 셈이다.
    따라서 어떤 수의 제곱 x^2보다 N이 작거나 같은 경우, (x-1)이 한 변의 길이가 됨.
    ex) N = 8, 3^2 = 9일때 작으므로 길이 = 2.

    단, 점의 갯수가 (길이-1)x(길이-1)에서 한 칸만 늘려도 되는 경우엔 길이x(길이-1) 형태로 구성하는게 더 효율적임.
    ex) N = 12일 경우...
    => 4^2보다 작으므로 길이는 3이 된다. 하지만 12 - 9 = 3이므로, 2x2 직사각형에서 한 칸만 늘려 2x3으로도 만들 수 있음.

    그림이 첨부되어 있는 설명글👉 https://wooriel.tistory.com/91
    """

    N = int(input())

    # N이 4이하일경우에도 직사각형은 최소 1x1 이어야 함. 바로 4 출력후 return
    if N <= 4:
        print(4)
        return

    length = 1

    for i in range(1, N + 1):
        num = i * i

        if num >= N:
            length = i - 1
            break

    if N - (length**2) <= length:
        print((length - 1) * 2 + length * 2)
    else:
        print(length * 4)


main()