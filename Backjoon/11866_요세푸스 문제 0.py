# 스택, 큐, 덱
# 메모리: 34008KB / 시간: 60ms

# 반대로 rotate 한 뒤 꺼내주면 된다.
from collections import deque


N, K = map(int, input().split())

dq = deque([*range(1, N+1)])
ret = []

while dq:
    dq.rotate(-K + 1)
    ret.append(dq.popleft())

print(f"<{', '.join(map(str, ret))}>")