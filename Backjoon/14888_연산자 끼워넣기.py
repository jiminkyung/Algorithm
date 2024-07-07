# 백트래킹
# AI선생님의 도움을 받은 풀이. 문제의 힌트는 사용 X

# 메모리: 31252KB / 시간: 80ms

import sys


input = sys.stdin.readline

input()
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
# operators = {oper: i for oper, i in zip(["+", "-", "x", "/"],map(int, input().split()))}

_max = float("-inf")
_min = float("inf")

def calculator(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -(abs(a) // b)
        else:
            return a // b

def insert_operator(idx, curr):
    global _max, _min

    if idx == len(arr):
        _max = max(_max, curr)
        _min = min(_min, curr)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            insert_operator(idx+1, calculator(curr, arr[idx], i))
            operators[i] += 1

insert_operator(1, arr[0])
sys.stdout.write(str(_max) + "\n" + str(_min))