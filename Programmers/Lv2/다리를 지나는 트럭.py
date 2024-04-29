"""
❌
모듈 안쓰고 풀기에 도전했지만 실패했다.
아래는 클로드를 통해 물어본 코드다. 참고로 정답률에 비해 정답 코드가 적은 문제였다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    """
    트럭들이 다리를 건너는 최소 시간을 계산하는 함수

    Args:
        bridge_length (int): 다리의 길이
        weight (int): 다리가 견딜 수 있는 최대 무게
        truck_weights (list): 트럭들의 무게를 담은 리스트

    Returns:
        int: 모든 트럭이 다리를 건너는 최소 시간
    """
    truck_weights = deque(truck_weights)  # 트럭 무게를 deque로 변환
    bridge = deque([0] * bridge_length)  # 다리를 나타내는 deque
    total_weight = 0  # 다리 위의 트럭 무게 합
    time = 0
    
    while bridge:
        # 다리를 건너는 과정을 시뮬레이션하는 반복문
        time += 1
        total_weight -= bridge.popleft()  # 다리를 건넌 트럭의 무게 제거
        
        if truck_weights:
            # 대기 중인 트럭이 있고, 다리에 올라갈 수 있는 경우
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                # 대기 중인 트럭이 있지만, 다리에 올라갈 수 없는 경우
                bridge.append(0)
    
    return time

"""
다리의 길이와 트럭이 다리를 건너는 시간의 관계:

bridge 변수는 다리를 나타내는 deque로, 다리의 길이만큼 0으로 초기화된다.
1. 다리를 건넌 트럭의 무게를 bridge.popleft()를 통해 제거
2. 대기 중인 트럭이 있고, 다리에 올라갈 수 있는 경우 bridge.append(truck)을 통해 트럭을 다리에 추가
3. 대기 중인 트럭이 있지만 다리에 올라갈 수 없는 경우 bridge.append(0)을 통해 0을 다리에 추가

이렇게 함으로써 bridge의 길이는 항상 다리의 길이와 같게 유지되며,
트럭이 다리에 진입하면 해당 트럭의 무게가 bridge에 추가되고,
다리를 완전히 건너면 bridge.popleft()를 통해 제거된다.
따라서 트럭이 다리를 건너는 데 걸리는 시간은 다리의 길이와 동일하게 유지된다.
"""

# 그리고 좋아요가 가장 많았던 정답 코드. 클래스로 구현한 풀이다. 멋있음.
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()