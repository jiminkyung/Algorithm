# 시뮬레이션
# 그리디 알고리즘
# 우선순위 큐


# 문제: https://www.acmicpc.net/problem/1417

# 1) 힙 사용
# 메모리: 35508KB / 시간: 52ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def main():
    N = int(input())

    dasom = int(input())
    cnt = 0
    heap = []

    # 인원이 한명이면 다솜이만 출마한것이므로 무조건 당선.
    if N == 1:
        print(0)
        return
    
    for _ in range(N-1):
        heappush(heap, -int(input()))
    
    # 매수한 표 + 다솜이의 기존 표가 최다 득표수가 될 때까지 반복
    while True:
        num = -heappop(heap)

        if num < dasom + cnt:
            break

        cnt += 1
        heappush(heap, -num+1)
    
    print(cnt)


main()


# 2) 굳이 힙을 사용하지 않아도 됨.
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    dasom = int(input())

    if N == 1:
        print(0)
        return

    votes = [int(input()) for _ in range(N-1)]
    cnt = 0

    while dasom + cnt <= max(votes):
        idx = votes.index(max(votes))  # 최다득표자의 인덱스 번호
        votes[idx] -= 1
        cnt += 1
    
    print(cnt)


main()