# 기하학


# 문제: https://www.acmicpc.net/problem/1002

# 거리 구할때 제곱근을 취하면 틀림... 관련글👉 https://www.acmicpc.net/board/view/142762
# 댓글대로 모두 제곱해서 구하니 통과했다.

# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def checking(x1, y1, r1, x2, y2, r2):
    distance = (x1 - x2)**2 + (y1 - y2)**2

    # 1. 두 원이 일치하고(중심 동일), 반지름이 같은 경우
    if distance == 0 and r1 == r2:
        return -1
    
    # 2. 두 점에서 교차하는 경우
    if abs(r1 - r2) ** 2 < distance < (r1 + r2) ** 2:
        return 2
    
    # 3. 한 점에서 교차하는 경우 (내/외접)
    if distance == (r1 + r2) ** 2 or distance == abs(r1 - r2) ** 2:
        return 1
    return 0


T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(checking(x1, y1, r1, x2, y2, r2))