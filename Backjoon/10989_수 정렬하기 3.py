# 정렬

# n = map(int, sys.stdin.readline())
# int(개행문자)는 가능하지만, 위의 경우엔 개행문자가 포함된 상태로 map()호출을 하기때문에 에러 발생.

# 메모리 초과...
import sys


input = sys.stdin.readline
N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

print(*nums, sep="\n")


# 재시도. 그러나 메모리 초과.
import sys


nums = [0] * 10001
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    nums[int(input())] += 1

print("\n".join(str(i) for i, cnt in enumerate(nums) if cnt for _ in range(cnt)))


# 다시 시도.
# 통과! 메모리: 31120KB / 시간: 8848ms
# ❌ join()은 리스트나 이터러블의 모든 요소를 하나의 문자열로 합치는 연산으로, 이 과정에서 메모리 사용량이 증가할 수 있다.
import sys


nums = [0] * 10001
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    nums[int(input())] += 1

for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)