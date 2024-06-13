# 정렬
# 시간: 80ms

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()
print(*nums, sep="\n")