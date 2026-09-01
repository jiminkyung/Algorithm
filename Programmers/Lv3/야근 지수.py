# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12927
from heapq import heappush, heappop


def solution(n: int, works: list[int]) -> int:
    # 🗝️ 최대한 균등하게 만들어주는게 포인트임.
    # 최대힙을 사용해서 가장 야근지수가 큰 값을 -1 처리해주는 과정을 n번 반복.
    heap = []

    for work in works:
        heappush(heap, -work)
    
    for _ in range(n):
        max_work = -heappop(heap)
        
        # 만약 남은 야근지수가 0이라면 멈춤.
        if max_work == 0:
            break

        heappush(heap, -(max_work-1))
    
    ret = sum(map(lambda x: x ** 2, heap))
    return ret