# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/1822

# 이분탐색 문제이긴 한데... set을 사용하는게 훨씬 빠르다.


# 1. set() 사용
# 메모리: 147600KB / 시간: 844ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ret = A - B
if len(ret):
    print(len(ret))
    print(*sorted(ret))
else:
    print(0)


# 2. 이분탐색 사용
# 메모리: 117360KB / 시간: 2044ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

def binary_search(target):
    start, end = 0, M-1
    
    while start <= end:
        mid = (start + end) // 2

        if B[mid] == target:
            return False
        elif B[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return True

ret = []

for a in A:
    if binary_search(a):
        ret.append(a)

if ret:
    print(len(ret), " ".join(map(str, ret)), sep="\n")
else:
    print(0)