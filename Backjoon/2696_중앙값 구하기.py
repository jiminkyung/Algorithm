# 자료 구조
# 우선순위 큐


# 문제: https://www.acmicpc.net/problem/2696

# 힙(heap)을 활용하는 기본적인 문제
# 나중에 힙 연습할때 다시 풀어볼만함

# 메모리: 35508KB / 시간: 48ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def main():
    for _ in range(int(input())):
        ret = solve()
        L = len(ret)
        print(L)
        for i in range(0, L, 10):
            print(*ret[i:min(i+10, L)])


def solve():
    M = int(input())
    seq = []

    for _ in range(M // 10 + 1):
        line = list(map(int, input().split()))
        seq.extend(line)

    max_heap = []  # 왼쪽: 최대힙
    min_heap = []  # 오른쪽: 최소힙
    # 중앙값보다 작거나 같은값들은 최대힙에, 큰 값들은 최소힙에 들어갈거임.
    # 중앙값이 항상 왼쪽에 존재하게끔 진행할거임.

    # 일단 첫번째값은 아묻따 최대힙(왼쪽)에 삽입
    heappush(max_heap, -seq[0])
    ret = [seq[0]]

    for i in range(1, M):
        num = seq[i]

        # 만약 현재까지의 중앙값(최대힙에서 가장 큰 값) 보다 작거나 같다면, 최대힙에 추가. 아니라면 최소힙에 추가.
        if -max_heap[0] >= num:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)
        
        # 1. 최소힙이 더 클 경우, 갯수가 동일해질때까지 최소힙의 원소를 최대힙에 삽입.
        while len(max_heap) < len(min_heap):
            num = heappop(min_heap)
            heappush(max_heap, -num)
        # 2. 최대힙 길이가 최소힙 길이보다 2 이상 클 경우, 차이가 1 ~ 0 이 될 때까지 최대힙 원소를 최소힙에 삽입.
        while len(max_heap) - len(min_heap) >= 2:
            num = -heappop(max_heap)
            heappush(min_heap, num)
        
        # 홀수번째라면 중앙값 출력
        if i % 2 == 0:
            ret.append(-max_heap[0])
    
    return ret


main()