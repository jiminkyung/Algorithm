# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1406

# 스택으로 풀어야 Python3로 통과 가능.
# 메모리: 41540KB / 시간: 260ms
from sys import stdin


input = stdin.readline

left = list(input().rstrip())
right = []

M = int(input())
for _ in range(M):
    cmd = input().rstrip().split()

    if cmd[0] == "L" and left:
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left.append(right.pop())
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])

print("".join(left + right[::-1]))


# 시간초과된 코드. 문자열 사용.
from sys import stdin


input = stdin.readline

word = input().rstrip()
M = int(input())

cursor = len(word)
for _ in range(M):
    cmd = input().rstrip().split()

    if cmd[0] == "L":
        if cursor == 0:
            continue
        cursor -= 1
    elif cmd[0] == "D":
        if cursor == len(word):
            continue
        cursor += 1
    elif cmd[0] == "B":
        word = word[:cursor-1] + word[cursor:]
        cursor -= 1
    else:  # "P $"
        word = word[:cursor] + cmd[1] + word[cursor:]
        cursor += 1

print(word)