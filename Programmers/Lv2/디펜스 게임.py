"""
힙(heap)을 사용하는 문제.

힙이란? => 최댓값/최솟값을 빨리 찾을 수 있도록 만들어진 완전이진트리 형식의 자료구조.
- 최소힙: 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 힙
- 최대힙: 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 힙

파이썬에서는 heapq 모듈을 통해 사용할 수 있다. 기본적으로는 최소힙.
- heappush(heap, item): item을 heap에 추가
- heappop(heap): heap에서 가장 작은 원소를 뽑아냄
"""

import heapq


def solution(n: int, k: int, enemy: list) -> int:
    """
    round: 통과한 라운드의 수
    enemies: 현재까지 상대한 적의 수
    """
    round = enemies = 0
    heap = []

    for e in enemy:
        heapq.heappush(heap, -e)
        enemies += e

        if enemies > n:
            if not k:
                break
            k -= 1
            enemies += heapq.heappop(heap)
        round += 1
    return round