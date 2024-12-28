# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/2467
# 투 포인터, 이분탐색 중 선택할 수 있는 문제다.
# BUT 투 포인터를 사용하는 편이 더 효율적임.

# 1. 이분탐색
# 메모리: 44748KB / 시간: 740ms
from sys import stdin


input = stdin.readline

N = int(input())
liquids = list(map(int, input().split()))  # 이미 정렬된 형태로 주어짐

min_diff = float("inf")
min_left = min_right = 0
flag = False  # 값이 0이라면 바로 종료할 수 있도록 판단

# 첫번째 용액: i, 두번째 용액: i+1~ 이므로 i의 범위를 N-2까지만 설정
for i in range(N-1):
    curr = liquids[i]

    start, end = i+1, N-1
    while start <= end:
        mid = (start + end) // 2
        diff = liquids[mid] + curr

        if abs(diff) < min_diff:
            min_diff = abs(diff)
            min_left = i
            min_right = mid
            
            if diff == 0:
                flag = True
                break
        
        if diff < 0:  # 두 용액의 합이 음수라면 새로운 용액을 더 큰 값으로
            start = mid + 1
        else:
            end = mid - 1
    
    if flag:
        break


print(liquids[min_left], liquids[min_right])


# ⭐2. 투 포인터
# 메모리: 44748KB / 시간: 116ms
from sys import stdin


input = stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left, right = 0, N-1
min_diff = abs(liquids[left] + liquids[right])
min_left, min_right = left, right

while left < right:
    diff = liquids[left] + liquids[right]

    if abs(diff) < min_diff:
        min_left = left
        min_right = right
        min_diff = abs(diff)

        if diff == 0:
            break
    
    if diff < 0:  # 두 용액의 합이 음수라면 새로운 용액을 더 큰 값으로
        left += 1
    else:
        right -= 1


print(liquids[min_left], liquids[min_right])