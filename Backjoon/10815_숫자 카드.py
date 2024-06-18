# 집합과 맵
# 메모리: 108848KB / 시간: 724ms

# 사이트에서는 통과 됨. vsc에서는 확인 불가.
# 입력 데이터가 큰 경우에는 readlines() 사용시 메모리 부족문제가 생길 수 있다.

import sys


nums = sys.stdin.readlines()

N, M = set(map(int, nums[1].split())), map(int, nums[3].split())

for i in M:
    print(int(i in N), end=" ")