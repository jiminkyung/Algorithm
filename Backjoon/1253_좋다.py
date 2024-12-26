# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/1253

# 투포인터로 푸는게 더 편한 문제같다.
# 메모리: 32412KB / 시간: 632ms
from sys import stdin


input = stdin.readline

N = int(input())
numbers = sorted(map(int, input().split()))

def two_pointer(target):
    left, right = 0, N-1

    while left < right:
        # left, right가 target과 겹치지 않도록 처리
        if left == target:
            left += 1
        if right == target:
            right -= 1
        
        if left == right:  # 처리 과정에서 left = right가 되면 break
            break

        two_sum = numbers[left] + numbers[right]
        if two_sum == numbers[target]:  # 좋은수 조건을 만족한다면 바로 True 반환.
            return True
        elif two_sum > numbers[target]:
            right -= 1
        else:
            left += 1
    return False


cnt = 0
# 타겟을 하나씩 지정해가며 해당 타켓값을 만족하는 경우가 있는지 체크
for target in range(N):
    cnt += two_pointer(target)

print(cnt)