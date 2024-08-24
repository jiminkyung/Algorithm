# 투 포인터

# 메모리: 42036KB / 시간: 100ms

from sys import stdin


input = stdin.readline
N = int(input())
nums = sorted(map(int, input().split()))

i, j = 0, N-1
ret = float("inf")  # 비교할 덧셈값
n1 = n2 = 0  # 출력할 원소값 1, 2

while i < j:
    num = nums[i] + nums[j]
    if num == 0:  # 두 원소를 더한값이 0이라면 i, j를 저장한 뒤 break
        n1, n2 = i, j
        break

    if abs(num) < abs(ret):  # 만약 더한값의 절댓값이 기존의 ret 절댓값보다 작다면,
        ret = num  # ret을 현재의 값으로 변경해준 뒤 i, j 재할당.
        n1, n2 = i, j

    if num > 0:  # 더한값이 0보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 한칸씩 미뤄준다.
        j -= 1
    else:
        i += 1

print(nums[n1], nums[n2])