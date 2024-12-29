# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/2143

# 이분탐색 대신 해시(딕셔너리)를 사용하는게 훨씬 효율적임.
# 이 문제는 해시가 맞는것같다. 이분탐색을 사용할 경우 코드가 지저분해진다...


# 1. 해시 + 이분탐색
# 메모리: 121828KB / 시간: 1680ms
from sys import stdin


input = stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

# 부배열 합의 쌍을 키값으로 하는 딕셔너리 생성
def make_dic(arr):
    arr_dic = {arr[0]: 1}
    arr_sum = [arr[0]]

    S = arr[0]
    for i in range(1, len(arr)):
        S += arr[i]
        arr_dic[S] = arr_dic.get(S, 0) + 1
        arr_sum.append(S)
        for j in range(i):
            tmp = S - arr_sum[j]
            arr_dic[tmp] = arr_dic.get(tmp, 0) + 1
    return arr_dic

A_dic = make_dic(A)
B_dic = make_dic(B)

A_keys = sorted(A_dic.keys())
B_keys = sorted(B_dic.keys())

total_cnt = 0

def binary_search(target):
    start, end = 0, len(B_keys)-1

    while start <= end:
        mid = (start + end) // 2

        if B_keys[mid] == target:
            return A_dic[T-target] * B_dic[B_keys[mid]]

        if B_keys[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for a in A_keys:
    total_cnt += binary_search(T - a)

print(total_cnt)


# 2. 해시
# 시간 순위 1위: https://www.acmicpc.net/source/85318604
# 시간 순위 2위: https://www.acmicpc.net/source/70613409
# 코드가 깔끔하니 나중에 다시 한 번 보면 좋을것같다.

# 메모리: 74400KB / 시간: 392ms
from sys import stdin


input = stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A_dic = {}

for i in range(n):
    S = 0
    for j in range(i, n):
        S += A[j]
        A_dic[S] = A_dic.get(S, 0) + 1

total_cnt = 0

for i in range(m):
    S = 0
    for j in range(i, m):
        S += B[j]
        total_cnt += A_dic.get(T-S, 0)

print(total_cnt)