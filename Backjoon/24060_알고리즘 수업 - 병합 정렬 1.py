# 재귀
# AI의 도움을 받은 문제. 병합정렬 구현.

# 메모리: 90208KB / 시간: 2216ms
from sys import stdin


input = stdin.readline

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    global count, K, result
    left = start
    right = mid + 1
    tmp = []

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1

    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= end:
        tmp.append(arr[right])
        right += 1

    i = start
    for t in range(len(tmp)):
        count += 1
        if count == K:
            result = tmp[t]
        arr[i] = tmp[t]
        i += 1

# 입력 받기
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 전역 변수 초기화
count = 0
result = -1

# 병합 정렬 수행
merge_sort(arr, 0, N-1)

# 결과 출력
print(result)


# 이진트리구조를 이용해서 수 알아내기. https://www.acmicpc.net/source/79738289
# 시간: 216ms
import math



def find(arr, n, k):
    def f(s, e, k):
        mid = (s+e+1) // 2
        left = check(mid-s)
        if left >= k:
            return f(s, mid, k)
    
        right = left + check(e-mid)
        if right >= k:
            return f(mid, e, k-left)
    
        return sorted(arr[s:e])[k - right - 1]
    
    
    def check(n):
        if not n:
            return 0
        
        a = math.floor(math.log2(n))
        b = n - (2 ** a)

        return a*(2**a) + (a + 2)*b

    
    if check(n) < k:
        return -1

    return f(0, n, k)


N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(find(arr, N, K))