# 문제집 - 0x08강 - 스택의 활용(수식의 괄호 쌍)


# 문제: https://www.acmicpc.net/problem/3986
# 🚨 AAA 같은 경우, 좋은 단어에 부합하지 않는다.

# 메모리: 31744KB / 시간: 108ms
from sys import stdin


input = stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

cnt = 0
for word in words:
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    cnt += int(not stack)

print(cnt)


# 좀 더 빠른 버전이 있길래 참고해봄.
# 참고👉 https://www.acmicpc.net/source/85559235
# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline

total_cnt = 0
for _ in range(int(input())):
    word = input().rstrip()
    A_cnt, B_cnt = word.count("A"), word.count("B")

    if A_cnt % 2 == 0 and B_cnt % 2 == 0:
        if word == word[::-1]:
            total_cnt += 1
        else:
            while "AA" in word or "BB" in word:
                if "AA" in word:
                    word = word.replace("AA", "")
                else:
                    word = word.replace("BB", "")
            total_cnt += int(not word)

print(total_cnt)