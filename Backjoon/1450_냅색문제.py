# 투 포인터

# Meet In The Middle 알고리즘을 사용하는 문제.
# 참고👉 https://ca.ramel.be/100 , https://hooongs.tistory.com/331


# 메모리: 34460KB / 시간: 120ms

from sys import stdin


input = stdin.readline
N, C = map(int, input().split())
things = list(map(int, input().split()))
ret = 0

left = things[:N//2]
right = things[N//2:]
left_sum = []
right_sum = []

def bruteforce(lst, sum_lst, idx, weight):
    if idx >= len(lst):
        sum_lst.append(weight)
        return
    bruteforce(lst, sum_lst, idx + 1, weight)  # 현재 물건을 건너뛰고 다음 물건으로.
    bruteforce(lst, sum_lst, idx + 1, weight + lst[idx])  # 현재 물건을 포함하고 다음 물건으로.


def binary_search(lst, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if lst[mid] <= target:
            start = mid + 1
        else:
            end = mid  # target보다 큰 첫 원소의 인덱스. 이 인덱스값은 target 이하인 원소의 갯수와 일치함.
    return end

bruteforce(left, left_sum, 0, 0)
bruteforce(right, right_sum, 0, 0)
right_sum.sort()

for l in left_sum:
    if C - l < 0:  # 가능한 무게에서 왼쪽 물건의 무게를 뺀 값이 0 이하라면 불가능.
        continue
    ret += binary_search(right_sum, C - l, 0, len(right_sum))  # 가능하다면, 정렬된 right_sum에서 C-l이하인 값의 수를 찾는다.

print(ret)


# 조합, 이분탐색 모듈을 사용한 풀이.
from itertools import combinations
from bisect import bisect_right 

# array 넣으면 부분집합 구하고 부분집합의 합의 list 반환하는 함수
# 두 부분에 대해서 가능한 모든 부분집합의 무게 합 구하기
def split_list(lst):
    result = []

    for i in range(len(lst) + 1): 
        for comb in combinations(lst, i):
            result.append(sum(comb))

    return result


def solution():

    # 입력 받기
    N, max_weight = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    # 물건 리스트 두 부분으로 나누기
    left_weights = weights[:N//2]
    right_weights = weights[N//2:]

    left_weights = split_list(left_weights)
    right_weights = split_list(right_weights)

    # 오른쪽 배열은 이진탐색(bisect)을 위해서 정렬돼있어야 함
    right_weights.sort()

    # 왼쪽 부분집합의 합을 하나씩 탐색하면서
    count = 0
    
    for left in left_weights:
        if left <= max_weight:
            # 오른쪽 부분집합에서 c를 넘지 않는 최대 가능한 값 찾기
            count += bisect_right(right_weights, max_weight - left)
    
    return count

    
print(solution())