# 메모리: 31252KB / 시간: 44ms

N, K = map(int, input().split())

root = int(N ** 0.5)
nums = set()

for i in range(1, root+1):
    if N % i == 0:
        nums.add(i)
        nums.add(N // i)

ret = sorted(nums)
print(ret[K-1] if len(ret) >= K else 0)