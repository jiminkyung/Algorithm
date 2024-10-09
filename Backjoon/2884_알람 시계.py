# 조건문


# 문제: https://www.acmicpc.net/problem/2884
# 메모리: 31120KB / 시간: 36ms
H, M = map(int, input().split())

time = H * 60 + M - 45
if time < 0:
    print(f"23 {60 + time}")
else:
    print(f"{time // 60} {time % 60}")