# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42628


from heapq import heappush, heappop


def solution(operations: list[str]) -> list[int, int]:
    max_heap, min_heap = [], []
    numbers = {}  # numbers[num]: 큐에 남아있는 num의 갯수

    for operation in operations:
        cmd, num = operation.split()
        num = int(num)

        # 최대힙과 최소힙으로 따로 관리되지만, 실제로는 한개의 큐에 존재하므로 상태를 맞춰줘야 함.
        # 최대힙에서 3 제거 -> numbers[3] 갯수 차감 -> 최소힙에서 3 이 뽑히더라도 이미 제거된 상태임을 알 수 있음.
        if cmd == "I":
            heappush(max_heap, -num)
            heappush(min_heap, num)
            numbers[num] = numbers.get(num, 0) + 1  # 해당 숫자의 갯수를 증가시킴
        else:
            # numbers로 큐에 남아있는 숫자 갯수를 확인해가며 최댓값/최솟값 추출
            if num == 1:
                while max_heap:
                    max_num = -heappop(max_heap)
                    
                    if numbers[max_num] > 0:
                        numbers[max_num] -= 1
                        break
            else:
                while min_heap:
                    min_num = heappop(min_heap)

                    if numbers[min_num] > 0:
                        numbers[min_num] -= 1
                        break
        
    ret = None

    # 큐가 비어있는 상태라면
    if all(val == 0 for val in numbers.values()):
        ret = [0, 0]
    else:
        # 🚨 모든 연산이 끝난 뒤에도 두 큐의 상태를 맞춰줘야 함. 최댓값/최솟값을 뽑아야 하기 때문.
        while numbers[-max_heap[0]] == 0:
            heappop(max_heap)
        while numbers[min_heap[0]] == 0:
            heappop(min_heap)

        max_num, min_num = -heappop(max_heap), heappop(min_heap)
        ret = [max_num, min_num]
    
    return ret