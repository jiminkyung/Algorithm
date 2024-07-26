# 이분 탐색

"""
절단할 수 있는 최소높이는 0,
필요한 나무의 길이 M의 범위가 1<= 이니까, 최대높이는 (가장 높은 나무-1)가 될것이다.
최대한 나무를 덜 자를 수 있도록 해야한다. 즉 높이가 높을수록 좋음.
"""

# 메모리: 150200KB / 시간: 2112ms

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cutting_trees(height):
    return sum(tree-height for tree in trees if tree > height)

def binary_search(target):
    start, end = 0, max(trees)-1
    ret = 0

    while start <= end:
        mid = (start + end) // 2

        if cutting_trees(mid) >= target:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ret

print(binary_search(M))


# Counter 모듈을 이용하면 더 단축시킬 수 있다. => 높이가 같은 나무가 여러개 있을 수 있으므로.
# 메모리: 113872KB / 시간: 420ms => 훨씬 단축됨!
from collections import Counter
from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

def cutting_trees(height):
    tmp = 0

    for h, cnt in trees.items():
        if h > height:
            tmp += (h - height) * cnt
    
    return tmp


def binary_search(target):
    start, end = 0, max(trees)-1
    ret = 0

    while start <= end:
        mid = (start + end) // 2

        if cutting_trees(mid) >= target:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ret

print(binary_search(M))