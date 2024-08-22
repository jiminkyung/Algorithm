# 투 포인터

# 메모리: 42036KB / 시간: 88ms

from sys import stdin


input = stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))
x = int(input())

ret = 0
i, j = 0, n-1

while i < j:
    if nums[i] + nums[j] == x:  # 더한값이 x와 같다면 i좌표를 오른쪽으로 한칸, j좌표를 왼쪽으로 한칸 옮겨준다.
        ret += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] > x:  # 크다면 j좌표만 왼쪽으로 한칸,
        j -= 1
    else:  # 작다면 i좌표만 오른쪽으로 한칸.
        i += 1

print(ret)


# 다른 좋은 방법. x값을 리스트에 추가 후, j좌표를 x의 인덱스-1로 설정하기.
# 메모리: 42036KB / 시간: 68ms
from sys import stdin


input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.append(x)
nums.sort()

ret = 0
i, j = 0, nums.index(x)-1

while i < j:
    if nums[i] + nums[j] == x:
        ret += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] > x:
        j -= 1
    else:
        i += 1

print(ret)