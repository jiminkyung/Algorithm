# 스택 2

# 오등큰수: 오른쪽에 있으면서 수열에서 등장한 횟수가 An의 횟수보다 큰 수 중 가장 왼쪽에 위치한 수. ㅋㅋ
# 메모리: 147028KB / 시간: 1664ms

from sys import stdin
from collections import Counter


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
count = Counter(A)  # k:v = A의 원소: 갯수

ret = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and count[A[stack[-1]]] < count[A[i]]:  # 스택이 존재하고 A[스택[-1]]의 갯수보다 A[현재 인덱스]가 클 때,
        ret[stack.pop()] = A[i]                         # ret[스택[-1]]을 A[현재 인덱스]값으로 변경
    stack.append(i)                                     # 스택에는 그대로 현재 인덱스값을 추가한다.

print(*ret)