# 누적 합

# 모듈러 연산을 응용한 풀이. AI 활용.
# 메모리: 142240KB / 시간: 624ms
"""
모듈러 연산
- A % M = B % M 일때, (A-B) % M = 0 이다.
- 즉, 다른 두 구간합의 나머지가 i로 동일할때, 두 구간합의 차는 M으로 나누어떨어진다.
"""
from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

curr = 0
count = [1] + [0]*M
ret = 0

for num in nums:
    curr = (curr + num) % M
    ret += count[curr]
    count[curr] += 1

print(ret)


# 348ms 코드. math 모듈을 사용... 모듈이 최고다.
import math


def solution():
    N, M, *nums = map(int, open(0, 'rb').read().rstrip().split())
        
    s = 0
    cnt = [0] * M
    for num in nums:
        cnt[s := (s + num) % M] += 1
    
    print(sum(math.comb(i, 2) for i in cnt) + cnt[0])


solution()