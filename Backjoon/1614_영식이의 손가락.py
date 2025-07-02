# 구현
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/1614
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    C = int(input())

    # 1-2-3-4-5-4-3-2 : 1-1, 2-2, 3-2, 4-2, 5-1
    # 8번을 셀 때의 패턴은 위와 같음

    ret = 0

    # C가 0이면 손가락번호 - 1만큼만 셀 수 있음.
    if C == 0:
        ret = N - 1
    # 1. 엄지일경우 C번만큼 패턴 반복 가능
    elif N == 1:
        ret = 8 * C
    # 2. 새끼일경우 C번만큼 패턴 반복 후 엄지~약지(4번)까지는 가능
    elif N == 5:
        ret = 8 * C + 4
    # 3. 나머지 손가락일경우, 패턴 하나당 두번씩 사용되므로 C // 2만큼 패턴 반복.
    # 나머지값이 0이라면 N번 손가락 직전까지 추가로 셀 수 있음.
    # 나머지값이 1이라면 새끼까지(+5) 간 후 역방향으로 N번 손가락 전까지 셀 수 있음.
    else:
        t = C // 2
        ret = 8 * t
        if C % 2 == 0:
            ret += N - 1
        else:
            ret += 5 + (4 - N)

    print(ret)


main()
