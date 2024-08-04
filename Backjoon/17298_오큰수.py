# 스택 2

# 오큰수: An의 오른쪽에 있으면서 큰 수 중 가장 왼쪽에 위치한 값
# 메모리: 155536KB / 시간: 984ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

ret = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:  # 스택이 존재하고 A[스택의 마지막 값(인덱스)]보다 현재 A[현재 인덱스]가 클때,
        ret[stack.pop()] = A[i]           # ret[인덱스]를 A[현재 인덱스]값으로 변경.
    stack.append(i)                       # 조건의 참거짓과 상관없이 현재 인덱스값을 스택에 추가.

print(*ret)