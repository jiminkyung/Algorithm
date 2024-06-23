# 스택, 큐, 덱
# 메모리: 31120KB / 시간: 44ms

from sys import stdin


input = stdin.readline

T = int(input())

def check_ps(string) -> bool:
    stack = []

    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    
    return bool(not stack)

for _ in range(T):
    ps = input().strip()  # stdin로 그냥 input값을 받아올땐 strip()을 꼭 써주자.
    
    print("YES" if check_ps(ps) else "NO")