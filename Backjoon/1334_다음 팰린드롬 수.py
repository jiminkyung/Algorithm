# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/1334

# 단순한 문제였는데 괜히 어렵게 생각해서 헤맸었음. 나중에 다시 풀어봐도 좋을 문제~
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    """
    1. 주어진 숫자를 절반으로 나눈다.
    2. 왼쪽 절반(left)을 뒤집어 붙인 후, 기존 값보다 크다면 정답으로 판정.
        - 홀수면 left의 마지막 숫자는 제외하고, 짝수면 전부 포함해서 뒤집음.
    3. 아니라면 왼쪽 절반의 숫자에 1을 더한다.
    4. 1을 더한 후 자릿수가 변경된다면 (999 -> 1000), 1 + 0*(길이-1) + 1 형태로 출력.
    5. 아니라면 2번과 같은 형식으로 출력하면 된다.
    """
    number = input().rstrip()

    L = len(number)
    half = (L + 1) // 2  # 길이가 홀수인 경우도 대비
    left = number[:half]

    if L % 2 == 0:
        pal = left + left[::-1]
    else:
        pal = left + left[:-1][::-1]

    # 1차적으로 만든 팰린드롬수가 기존 수보다 크다면 출력
    if pal > number:
        print(pal)
        return

    # 아니라면, 왼쪽 절반에 +1 처리
    left = str(int(left) + 1)

    # 자릿수가 바뀐다면 앞뒤로 1을 넣어주고 사이엔 (길이-1)만큼의 0을 넣어 출력
    if len(left) > half:
        print("1" + "0" * (L - 1) + "1")
        return

    if L % 2 == 0:
        pal = left + left[::-1]
    else:
        pal = left + left[:-1][::-1]

    print(pal)


main()