# 스택, 큐, 덱
# 메모리: 55044KB / 시간: 200ms

from collections import deque


N = int(input())

dq = deque([i for i in range(1, N+1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(*dq)


# 효율성 최고 숏코딩.
"""
- 2 * (N - 가장 가까운 이전 2의 거듭제곱)
- N이 2의 거듭제곱일 때 (2, 4, 8, 16...), 마지막 남는 카드는 N 자체다.
- 그 외의 경우, 결과는 이전 2의 거듭제곱부터 시작해 2씩 증가.
- N을 2진수로 표현했을 때, 가장 왼쪽 비트를 제외한 나머지를 왼쪽으로 한 칸 시프트하고 맨 오른쪽에 1을 추가한 값과 같다.
"""
n,m = int(input()), 1
while m<n: # O(logn)
    m *= 2
print(2*n-m)