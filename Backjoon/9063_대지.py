# 메모리: 35060KB / 시간: 2844ms

N = int(input())
x, y = [], []

for _ in range(N):
    nx, ny = map(int, input().split())
    x.append(nx)
    y.append(ny)

print((max(x)-min(x))*(max(y)-min(y)))