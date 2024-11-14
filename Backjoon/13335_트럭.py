# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/13335

# while문 작성할때 버벅거려서 결국 다른 풀이를 참고했다...ㅜㅜ
# 참고👉 https://velog.io/@highcho/Algorithm-bakejoon-13335

# 메모리: 34160KB / 시간: 80ms
from sys import stdin
from collections import deque


input = stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
time = 0

# 다리의 길이만큼 [0]으로 이루어진 deque 생성
bridge = deque([0] * w)

while trucks:
    time += 1
    bridge.popleft()
    if sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)

print(time + len(bridge))