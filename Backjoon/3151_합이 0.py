# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/3151

# 이분탐색으로 분류되어있지만 투 포인터로 풀어야 하는 문제다.
# 이분탐색을 사용하면 시간초과가 난다...

# 메모리: 33432KB / 시간: 5236ms
from sys import stdin


input = stdin.readline

N = int(input())
A = sorted(map(int, input().split()))


# 2. 투 포인터 실행함수.
# left, right에 해당되는 값을 더한 후 target값과 같다면 카운트한다.
def two_pointer(left, right, target):
    cnt = 0

    while left < right:
        stat = A[left] + A[right]

        # target값과 같은경우
        if stat == target:
            # left == right라면 같은 수 이므로 left부터 right까지의 갯수를 구한다.
            # 구한 갯수에서 2개를 뽑는 조합을 계산 후 카운트에 더하기.
            if A[left] == A[right]:
                tmp = right - left + 1
                cnt += tmp * (tmp-1) // 2  # tmp개에서 2개를 뽑는 경우의 수
                break

            # left != right라면,
            # left와 같은 수가 반복되는 마지막 위치를, right와 같은 수가 반복되는 첫번째 위치를 찾을때까지 포인터를 이동시킨다.
            l_cnt = r_cnt = 1
            while A[left] == A[left+1]:
                l_cnt += 1
                left += 1
            while A[right] == A[right-1]:
                r_cnt += 1
                right -= 1

            cnt += l_cnt * r_cnt  # left의 중복 갯수 * right의 중복 갯수 -> 조합의 수
            left += 1
            right -= 1

        elif stat < target:
            left += 1
        else:
            right -= 1

    return cnt

ret = 0
# 1. 세 수 a, b, c 중 a를 선택하고 b, c를 투 포인터로 탐색한다.
# 범위는 현재 수+1 ~ 마지막까지
for i in range(N-2):
    ret += two_pointer(i+1, N-1, -A[i])

print(ret)