"""
효율성 검사가 있는 문제.
힙(Heap)문제인데, 모듈을 사용해야 하기 때문에 AI의 도움을 빌렸다.
"""

# 효율성 탈락
def solution(scoville, K):
    ret = 0
    while not all(s >= K for s in scoville):
        if len(scoville) < 2:
            return -1
        
        scoville.sort()
        ret += 1
        m1 = scoville.pop(0)
        m2 = scoville.pop(0)
        m = m1 + m2 * 2
        scoville.insert(0, m)
    return ret

# 힙을 사용하는 버전
import heapq

def solution(scoville, K):
    ret = 0
    heapq.heapify(scoville)  # scoville 리스트를 최소 힙으로 변환
    
    while scoville[0] < K:  # 최소 값이 K 이상이 될 때까지 반복
        if len(scoville) < 2:
            return -1  # 불가능한 경우 -1 반환
        
        m1 = heapq.heappop(scoville)  # 최소 값 두 개 꺼내기
        m2 = heapq.heappop(scoville)
        
        m = m1 + m2 * 2  # 새로운 스코빌 지수 계산
        heapq.heappush(scoville, m)  # 새로운 스코빌 지수를 최소 힙에 추가
        
        ret += 1
    
    return ret