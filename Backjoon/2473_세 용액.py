# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/2473
# 메모리: 33564KB / 시간: 2468ms
from sys import stdin


input = stdin.readline

N = int(input())
liquids = sorted(map(int, input().split()))

min_sum = float("inf")
ret = 0

def two_pointer(left, right, curr):
    global min_sum, ret

    while left < right:
        curr_sum = liquids[left] + liquids[right] + curr

        if abs(curr_sum) < min_sum:
            min_sum = abs(curr_sum)
            ret = (curr, liquids[left], liquids[right])

            if curr_sum == 0:  # 합이 0이라면 더이상 찾을 필요가 없으므로 프로그램 종료
                print(*sorted(ret))
                exit()
        
        if curr_sum < 0:
            left += 1
        else:
            right -= 1


for i in range(N-2):
    two_pointer(i+1, N-1, liquids[i])

print(*sorted(ret))


# 실행시간 1위 코드.
# 산성/알칼리로 분리한 뒤 음수2 + 양수1, 음수1 + 양수2 조합으로 체크하는 방식이다.
# 출처👉 https://www.acmicpc.net/source/71894068
'''
산성 2, 알칼리 1
산성 1, 알칼리 2
산성 3
알칼리 3
'''

import sys

N = int(input())

solutions = list(sorted(map(int, sys.stdin.readline().split())))

alkali = []
acid = []

acid_start = len(solutions)
for i in range(N):
    if solutions[i] > 0:
        acid_start = i
        break

alkali = []
if acid_start > 0:
    alkali = solutions[acid_start-1::-1]
acid = solutions[acid_start:]

min_sum = sys.maxsize
answer = []

if len(alkali) >= 3:
    min_sum = -(alkali[0] + alkali[1] + alkali[2])
    answer = alkali[2::-1]

if len(acid) >= 3 and min_sum > acid[0] + acid[1] + acid[2]:
    min_sum = acid[0] + acid[1] + acid[2]
    answer = acid[:3]

if len(alkali) >= 2 and acid:
    for mid_index in range(len(alkali)-1):
        alkali_index = mid_index + 1
        acid_index = 0

        while alkali_index < len(alkali) and acid_index < len(acid):
            if min_sum == 0:
                break

            solutions_sum = abs(alkali[alkali_index] + alkali[mid_index] + acid[acid_index])
            if min_sum > solutions_sum:
                min_sum = solutions_sum
                answer = [alkali[alkali_index], alkali[mid_index], acid[acid_index]]

            if -(alkali[alkali_index] + alkali[mid_index]) > acid[acid_index]:
                acid_index += 1
            else:
                alkali_index += 1

if len(acid) >= 2 and alkali:
    for mid_index in range(len(acid)-1):
        acid_index = mid_index + 1
        alkali_index = 0

        while alkali_index < len(alkali) and acid_index < len(acid):
            if min_sum == 0:
                break

            solutions_sum = abs(alkali[alkali_index] + acid[mid_index] + acid[acid_index])
            if min_sum > solutions_sum:
                min_sum = solutions_sum
                answer = [alkali[alkali_index], acid[mid_index], acid[acid_index]]

            if -alkali[alkali_index] > acid[mid_index] + acid[acid_index]:
                acid_index += 1
            else:
                alkali_index += 1

print(*sorted(answer))