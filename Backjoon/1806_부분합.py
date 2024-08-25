# 투 포인터

# 투 포인터로 LIS를 어떻게 구하느냐...
# 71%에서 실패.
from sys import stdin


input = stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = right = 0
curr = 0
ret = N+1

while right < N:  # 마지막 원소를 제대로 검사하지 못할 수 있음.
    if curr < S:
        curr += nums[right]
        right += 1
    else:
        ret = min(ret, right-left)
        curr -= nums[left]
        left += 1

print(ret if ret != N+1 else 0)


"""
반례
10 10
1 1 1 1 1 1 1 1 1 10
>> 1
"""
# 통과되는 버전. 참고👉 https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1806%EB%B2%88-%EB%B6%80%EB%B6%84%ED%95%A9
# 메모리: 42204KB / 시간: 104ms
from sys import stdin


input = stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = right = 0
curr = 0
ret = N + 1

while True:
    if curr >= S:
        ret = min(ret, right - left)
        curr -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        curr += nums[right]
        right += 1

print(ret if ret != N + 1 else 0)