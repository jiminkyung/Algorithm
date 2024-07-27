# 이분 탐색

"""
집 하나당 한개의 공유기만 설치 가능.
두 공유기 사이의 최대 거리를 구해야함.

우선 집 좌표들을 정렬해줘야한다.
최소거리는 가장 인접한 집 사이의 거리, 최대거리는 첫번째 집과 마지막 집 사이의 거리.
만약 mid(가운데값)으로 공유기 C대 설치가 가능하다면, 거리를 더 늘리기.(start 지점 = mid + 1로 변경)
불가능하다면 줄이기.

해당 distance가 가능한지 체킹하는 함수(checking_distance)짜기가 애매했다.
"""

# 메모리: 40412KB / 시간: 256ms

from sys import stdin


input = stdin.readline
N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

min_distance = min(x2 - x1 for x1, x2 in zip(houses, houses[1:]))

def checking_distance(distance):
    """
    일단 한대는 무조건 설치하고 시작하니까 cnt는 1로 설정.
    첫번째 집을 포인트 삼아서 두번째집부터 마지막집까지 순회.
    만약, 현재 집과 포인트 사이의 거리가 distance보다 크다면,(조건 만족)
    cnt를 1 추가시킨 뒤 포인트를 현재 집으로 재할당한다.
    cnt가 C를 넘어서면 True 반환. 그러지 못한다면 False.
    """
    cnt = 1
    point = houses[0]

    for house in houses[1:]:
        if (house - point) >= distance:
            cnt += 1
            point = house
            if cnt >= C:
                return True
    return False

def binary_search():
    start, end = min_distance, houses[-1]-houses[0]
    ret = 0

    while start <= end:
        mid = (start + end) // 2

        if checking_distance(mid):
            ret = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ret

print(binary_search())


# 시간이 104ms인 코드.
# 함수 f()가 효율적. 초기 범위 설정을 E = (끝집 - 첫번째집) // (C-1) + 1 로 작성. (C개의 공유기를 설치할때, 간격은 C-1가 됨.)
# mid+1, mid-1 대신 while 조건을 end > start+1 로 설정해줌.
from sys import stdin
n, c = map(int, input().split())
x = [int(y) for y in stdin.read().splitlines()]
x.sort()
def f(d):
    count, val = 1, x[0]+d
    for h in x:
        if h>=val:
            count, val = count+1, h+d
    return count
B, E = 1, (x[-1]-x[0])//(c-1)+1
while E>B+1:
    M = (B+E)//2
    B, E = (M, E) if f(M)>=c else (B, M)
print(B)