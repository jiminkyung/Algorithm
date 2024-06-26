# 스택, 큐, 덱
# 메모리: 34016KB / 시간: 64ms

"""
헷갈렸던 문제다.

문제에선 쪽지에 적힌 정수 N이 양수일경우, 오른쪽으로 N. 음수일경우 왼쪽으로 N.
하지만 실제로는 양수일경우 왼쪽으로 rotate, 음수일경우 오른쪽으로 rotate 되어야 함.

- 양수: 현재 위치 제외, 제거된 현재 위치 보정
- 음수: 그대로 이동 (원형 구조에서의 상대적 위치 유지), 이미 제거되어 보정 불필요
"""
from collections import deque
import sys


cmd = iter(sys.stdin.read().split())
next(cmd)

dq = deque(enumerate(map(int, cmd), start=1))
ret = []

while dq:
    idx, move = dq.popleft()
    ret.append(idx)

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(-move)

print(*ret)