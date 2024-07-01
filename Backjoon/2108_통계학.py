# 심화 2

# 시간 초과.
from sys import stdin


N = int(stdin.readline())

nums = list(map(int, stdin.read().split()))
nums.sort()

count = {i: nums.count(i) for i in set(nums)}

max_count = max(count.values())
mode = [num for num, cnt in count.items() if cnt == max_count]

if len(mode) == 1:
    mode_ret = mode[0]
else:
    mode_ret = mode[1]

ret = [round(sum(nums) / N), nums[N//2], mode_ret, max(nums)-min(nums)]
print(*ret, sep="\n")


# 다시 시도... Counter 함수 사용.
# 메모리: 90504KB / 시간: 348ms
from sys import stdin
from collections import Counter


N = int(stdin.readline())
nums = list(map(int, stdin.read().split()))

nums.sort()

count = Counter(nums)

max_num = max(count.values())
mode = [num for num, cnt in count.items() if cnt == max_num]
mode_ret = mode[0] if len(mode) == 1 else mode[1]

print(round(sum(nums)/N), nums[N//2], mode_ret, nums[-1]-nums[0], sep="\n")