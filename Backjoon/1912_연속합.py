# 동적 계획법 1

# 카데인 알고리즘 사용
# 메모리: 38828KB / 시간: 92ms

import sys


input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

ret = float("-inf")
curr = 0

for num in nums:
    curr = max(num, curr + num)
    ret = max(ret, curr)

print(ret)


# 절약하기 => 88ms
import sys


input = sys.stdin.readline

input()
nums = list(map(int, input().split()))

ret = float("-inf")
curr = 0

def kadane(lst):
    global curr, ret

    for num in lst:
        curr = max(num, curr + num)
        ret = max(ret, curr)
    
    return ret

print(kadane(nums))


# 더 간단하게 비교하는 방법 => 56ms!
# curr값이 음수라면 0으로 리셋 후 num으로, 아니라면 계속 더해주기.
# 수학적으로 정확함. 하지만 명시적이지 않음.
import sys


input = sys.stdin.readline

input()
nums = list(map(int, input().split()))

ret = float("-inf")
curr = float("-inf")

def kadane(lst):
    global curr, ret

    for num in lst:
        curr = (curr if curr > 0 else 0) + num
        ret = ret if ret > curr else curr
    
    return ret

print(kadane(nums))