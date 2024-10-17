# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/10828

# 예전에 풀었던 28279_덱2 와 비슷하게 풀이.
# 메모리: 32140KB / 시간: 36ms
from sys import stdin


# iter()함수로 저장된 값들은 한번 출력되면 끝.
# 따라서 아래 for문으로 순회중 next(cmd)를 사용하면 c 다음값이 출력됨.
cmd = iter(stdin.read().split())
next(cmd)

stack = []

for c in cmd:
    if c == "push":
        stack.append(next(cmd))
    elif c == "pop":
        print(stack.pop() if stack else -1)
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        print(int(not stack))
    else:
        print(stack[-1] if stack else -1)