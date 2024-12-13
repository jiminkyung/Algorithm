# 수학


# 문제: https://www.acmicpc.net/problem/1009
# 반례👉 https://www.acmicpc.net/board/view/153411
# 거듭제곱의 일의 자리 구하기👉 https://www.acmicpc.net/board/view/150353

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline


number = {2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]}
same_number = {1, 5, 6}

for _ in range(int(input())):
    a, b = map(int, input().split())
    ret = 0

    a %= 10

    if a in same_number:
        ret = a
    elif a == 0:
        ret = 10
    else:
        ret = number[a][b % len(number[a]) - 1]
    
    print(ret)