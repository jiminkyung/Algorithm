# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42627


# 최소 힙 문제
from heapq import heappush, heappop


def solution(jobs: list[list[int, int]]) -> int:
    jobs = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    jobs.sort()

    heap = []
    # time: 이전 작업이 끝나는 시간, total: 각 작업의 반환시간 합
    time = total = idx = 0

    while idx < len(jobs) or heap:
        # idx번째 작업의 시작시간이 이전 작업의 종료시간 이하일때까지 힙에 추가
        while idx < len(jobs) and jobs[idx][0] <= time:
            s, l, i = jobs[idx]
            heappush(heap, (l, s, i))
            idx += 1
        
        # 대기중인 작업이 없다면 idx번째 작업을 바로 시작하고 다음 턴으로 넘어감
        if not heap:
            time = jobs[idx][0]
            continue

        # 이전 작업이 끝난 후, 대기중인 작업들 중 우선순위가 가장 높은것을 뽑아냄
        l, s, i = heappop(heap)

        # 현재 뽑아낸 작업의 소요시간을 time에 적용 -> 다음 턴에서 "이전 작업의 종료시간"으로 사용
        time += l
        total += time - s  # 반환시간(끝나는 시간 - 시작 시간) 계산 후 total에 더해줌
    
    return total // len(jobs)  # 반환시간의 평균


# for문을 사용한 풀이. 사실 이 문제는 while문으로 푸는게 더 적절하다.
# 하지만 처음엔 for문으로 접근했던지라... 계속 풀어봄.
# 도움이 됐던 반례 ↓
# [[0, 5], [2, 5], [3, 5], [20, 3]] -> 정답: 7
from heapq import heappush, heappop


def solution(jobs: list[list[int, int]]) -> int:
    jobs = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    jobs.sort()
    times = [0] * len(jobs)  # time[x]: x번 작업의 반환시간

    heap = []
    time = 0  # 이전 작업이 끝나는 시간

    for i in range(len(jobs)):
        s, l, idx = jobs[i] 

        # 현재 작업이 time 이하라면 힙에 추가 후 넘어감
        if s <= time:
            heappush(heap, (l, s, idx))
            continue

        # 대기중인 작업이 없을 경우 현재 작업을 바로 실행, 시간 계산 후 넘어감
        if not heap:
            time = max(time, s) + l  # 현재 작업의 시작시간이 이전 작업의 종료시간보다 클 수도 있으므로, max로 더 큰 값을 정한 뒤 계산.
            times[idx] = time - s
            continue

        # 현재 작업이 time보다 크고, 대기중인 작업이 존재할때까지 pop 반복
        while heap and time <= s:
            _l, _s, _idx = heappop(heap)
            time = max(time, _s) + _l
            times[_idx] = time - _s

        # 현재 작업을 힙에 추가
        heappush(heap, (l, s, idx))

    # 힙이 남아있다면 계속 pop 진행
    while heap:
        l, s, idx = heappop(heap)

        time = max(time, s) + l
        times[idx] = time - s
    
    return sum(times) // len(times)


