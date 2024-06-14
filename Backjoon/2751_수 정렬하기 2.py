# 정렬

# 시간초과.
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()
print(*nums, sep="\n")


# 두번째 시도. sys 모듈을 사용하면 수행시간이 줄어든다.
# 메모리: 96512KB / 시간: 1280ms
import sys


N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

print(*nums, sep="\n")


# 효율적인 코드 발견. 출처👉 https://develop247.tistory.com/347
# 메모리: 125704KB / 시간: 692ms
# 시간은 절반 가까이 줄어들었지만, 메모리 효율성이 떨어진다.
nums = [None] * 2000001
n = map(int, open(0))

next(n)
for i in n:
    nums[i] = 1

print("\n".join(str(j) for j in range(-1000000, 1000001) if nums[j]))