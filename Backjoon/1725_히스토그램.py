# 스택 2

# 참고: https://eunsun-zizone-zzang.tistory.com/70
# 메모리: 41900KB / 시간: 132ms

from sys import stdin


input = stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]

stack = []
ret = 0

for i in range(N):
    idx = i  # 현재 막대의 시작 인덱스 (스택이 비워질 경우 사용)
    while stack and stack[-1][1] > heights[i]:  # 스택이 비어있지 않고, 스택의 top에 있는 막대의 높이가 현재 막대보다 높은 경우
        idx, height = stack.pop()
        box = (i - idx) * height  # 꺼낸 막대를 오른쪽 경계로 하는 직사각형의 넓이 계산
        ret = max(ret, box)
    stack.append((idx, heights[i]))  # 현재 막대 정보를 스택에 추가 (이전에 pop된 막대들 중 가장 왼쪽 인덱스 사용)

while stack:  # 스택에 남아있는 막대들 처리 (히스토그램의 끝까지 확장 가능한 직사각형들)
    idx, height = stack.pop()
    box = (N - idx) * height
    ret = max(ret, box)

print(ret)