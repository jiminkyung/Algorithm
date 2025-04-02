# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1263
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # 마감시간 기준으로 내림차순 정렬
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x: -x[1])

    time = 1000001  # 🚨24시간제가 아님. 최대 시간은 1000000.

    # 마감시간 - 걸리는시간 => 해당 일을 최대한 늦게 시작할 수 있는 시간
    # (마감시간, 이전 최소 시작시간) 중 더 작은 값을 선택,
    # 해당 값에서 걸리는시간을 뺀 값을 새로운 최소 시작시간으로 갱신한다.
    for t, s in lst:
        time = min(time, s) - t
    
    print(time if time >= 0 else -1)


main()