# 문제집 - 0x03강 - 배열


# 문제: https://www.acmicpc.net/problem/1475
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


plastic = stdin.readline().rstrip().replace("6", "9")
number = [0] * 10

for p in plastic:
    number[int(p)] += 1

number[9] = number[9] // 2 + number[9] % 2
print(max(number))


# 실행시간, 메모리 1위인 코드.
# 6과 9를 균등하게 분배한다.
import sys


def main(n):
    arr = [0 for i in range(10)]

    for x in list(str(n)):
        arr[int(x)] += 1

    t69 = arr[6] + arr[9]
    arr[6] = t69 // 2
    arr[9] = t69 - arr[6]

    return max(arr)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(main(n))