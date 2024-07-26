# 이분 탐색

"""
이분탐색이니까 일단 정렬.
1부터 랜선의 길이 중 가장 큰 길이까지를 범위로 잡고,
중간값이 N보다 크다면 start 지점을 중간+1로 변경.
더 큰 길이값을 찾는다.
갯수가 N이상이라면 길이를 늘려가면서 검사하므로 max()로 따로 점검해줄 필요 없음.
또, 재귀적으로 체크하는것보다 while문을 사용하는게 더 명확하고 효율적.
"""

# 메모리: 31120KB / 시간: 68ms

from sys import stdin


input = stdin.readline
K, N = map(int, input().split())
lines = sorted(int(input()) for _ in range(K))

def dividing(length):
    return sum(line//length for line in lines)

def checking_lines(target):
    start, end = 1, lines[-1]
    ret = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = dividing(mid)

        if cnt >= target:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ret

print(checking_lines(N))