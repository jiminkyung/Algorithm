# 스택, 큐, 덱
# 메모리: 71112KB / 시간: 1040ms

# 2번 맨 위의 정수를 빼고 출력한다 => 맨 위의 정수를 "빼고", 그 수를 "출력한다."
from sys import stdin


input = stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command, *num = input().split()

    if command == "1":
        stack.append(int(num[0]))
    elif command == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "3":
        print(len(stack))
    elif command == "4":
        print(int(not stack))
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)