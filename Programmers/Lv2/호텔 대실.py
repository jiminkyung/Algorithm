# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 최소 힙을 사용해야 하는 문제.
from heapq import heappush, heappop


def solution(book_time: list[list[str]]):
    times = []
    
    # 시간을 분 단위로 변환하여 (입실시간, 퇴실시간+10) 형태로 저장.
    for start, end in book_time:
        hh, mm = map(int, start.split(":"))
        start_time = hh * 60 + mm
        hh, mm = map(int, end.split(":"))
        end_time = hh * 60 + mm + 10
        
        times.append((start_time, end_time))
    
    # 오름차순 정렬 후 힙을 사용하여 계산.
    times.sort()
    heap = []
    
    for start, end in times:
        # 힙 안에 존재하는 값은 어떤 대실의 퇴실시간임.
        # 가장 빨리 끝나는 시간이 현재 시작 시간보다 작거나 같다면, 이 방을 사용할 수 있음.
        if heap and heap[0] <= start:
            heappop(heap)
        heappush(heap, end)
    return len(heap)