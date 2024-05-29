# 도화지 크기 = 가로세로 100

paper = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for k in range(y, y+10):
            paper[i][k] = 1

ret = sum(sum(row) for row in paper)
print(ret)