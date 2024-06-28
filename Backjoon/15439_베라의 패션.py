# 조합론
# 메모리: 31120KB / 시간: 32ms

# 가능한 경우: 상의 N개와 하의 N-1개 or 하의 N개와 상의 N-1개.
N = int(input())
print(N * (N-1))