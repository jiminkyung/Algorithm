# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/16637
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
lst = list(input().rstrip())
max_val = float("-inf")  # 🚨 0으로 설정하면 피본다. 최댓값이 음수일수도 있음.


def calculate(left, op, right):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    else:
        return left * right


def dfs(idx, curr_val):
    global max_val

    if idx >= N:
        max_val = max(max_val, curr_val)
        return
    
    # 괄호 없이 계산하는 경우
    nxt_val = calculate(curr_val, lst[idx], int(lst[idx+1]))
    dfs(idx+2, nxt_val)

    # 괄호를 사용해서 계산하는 경우
    if idx+2 < N:
        paren_val = calculate(int(lst[idx+1]), lst[idx+2], int(lst[idx+3]))
        nxt_val = calculate(curr_val, lst[idx], paren_val)
        dfs(idx+4, nxt_val)


dfs(1, int(lst[0]))
print(max_val)