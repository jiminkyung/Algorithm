# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/11000

# 우선순위 큐(heapq)를 왜 사용하지..? 했다가 결국 풀이를 찾아봤다.
# 참고👉 https://eunsun-zizone-zzang.tistory.com/64

# 메모리: 62456KB / 시간: 292ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
# 1. 시작시간이 빠른 순서대로, 종료시간이 빠른 순서대로 정렬
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort()

# 2. 힙에 가장 빨리 시작하는 수업의 종료시간을 넣어두고 순회
heap = [classes[0][1]]

# 3. 만약 힙의 "가장 빨리시작하는 수업의 종료시간" 보다 i의 시작시간이 늦거나 같다면 pop, i의 종료시간 push
# => 한 강의실에서 계속 진행할 수 있다는 소리임
# 그렇지 않다면 i의 종료시간 push만 진행
# => 다른 강의실을 사용해야 함
for i in range(1, N):
    if heap[0] <= classes[i][0]:
        heappop(heap)
    heappush(heap, classes[i][1])

print(len(heap))