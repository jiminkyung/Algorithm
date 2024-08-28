# 동적 계획법과 최단거리 역추적


# 14002_가장 긴 증가하는 부분 수열 4 의 답을 제출하면 시간초과다.
# 참고👉 https://onn5.tistory.com/37

# 메모리: 227164KB / 시간: 2488ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]  # 일반적인 LIS가 아닌, LIS의 길이만을 계산하기 위해 만들어진 리스트 <- 그리디 활용?
dp = [(0, A[0])]  # 각 원소가 LIS에서 위치하는 값과 실제 값을 저장. (인덱스, 원소값)

# 이분 탐색 함수 -> 변경할 LIS값의 인덱스를 반환함
def binary_search(target):
    start = 0
    end = len(LIS) - 1

    while start < end:
        mid = (start + end) // 2

        if LIS[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

for i in range(1, N):
    if A[i] > LIS[-1]:  # 현재 값이 LIS의 마지막 값보다 크다면 그대로 LIS, dp에 추가한다.
        LIS.append(A[i])
        dp.append((len(LIS)-1, A[i]))
    else:  # 작다면, 이분탐색 함수로 변경할 LIS값의 인덱스를 구한다.
        idx = binary_search(A[i])
        LIS[idx] = A[i]  # 해당 LIS값을 현재 값으로 변경하고, dp에 (구한 인덱스, 현재 값)을 추가한다.
        dp.append((idx, A[i]))

last_idx = len(LIS) - 1  # 탐색 시작을 위한 인덱스값. LIS의 길이값 - 1
ret_lst = []  # 결과를 저장할 리스트
for i in range(len(dp)-1, -1, -1):  # 끝부터 0까지 순회.
    if dp[i][0] == last_idx:  # 만약 last_idx값과 dp[i]의 인덱스값(LIS에서의 위치)가 같다면,
        ret_lst.append(dp[i][1])  # 결과리스트에 실제 값을 추가하고 last_idx를 1 감소시킨다.
        last_idx -= 1

print(len(LIS))
print(*ret_lst[::-1])


# bisect 모듈을 사용한 풀이. 생각보다 많이들 쓴다.
# -float('inf')로 초기화한 대신 LIS의 길이값을 출력할 때 -1을 해줌.
import sys
from bisect import bisect_left
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))

dp_table=[-float('inf')]
store=[]

for i in L:
    if dp_table[-1]<i:
        dp_table.append(i)  
        store.append((len(dp_table)-1,i))
    else:
        pos=bisect_left(dp_table, i)
        dp_table[pos] = i
        store.append((pos,i))

index=len(dp_table)-1
print(index)

result=[]
for i in range(len(store)-1,-1,-1):
    if store[i][0]==index:
        result.append(store[i][1])
        index-=1

print(*result[::-1])