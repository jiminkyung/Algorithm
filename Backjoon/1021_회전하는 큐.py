# 문제집 - 0x07강 - 덱


# 문제: https://www.acmicpc.net/problem/1021
# 메모리: 34008KB / 시간: 60ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())
queue = deque(list(range(1, N+1)))
order = list(map(int, input().split()))

total_cnt = 0
for o in order:
    cnt = 0  # 한칸 이동한 횟수
    while queue[0] != o:
        queue.rotate(1)
        cnt += 1
    total_cnt += min(cnt, len(queue)-cnt)  # 왼쪽으로 이동한 횟수와 오른쪽으로 이동한 횟수 중 더 작은값을 total_cnt에 추가
    queue.popleft()

print(total_cnt)


# 실행시간, 메모리 모두 더 효율적인 코드.
# 단순하게 리스트 슬라이싱을 사용함.
import sys

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    target = list(map(int, sys.stdin.readline().strip().split()))

    ls = [i for i in range(1, N+1)]

    res = 0
    for t in target:
        i = ls.index(t)
        # 1번
        if ls[0] == t:
            ls = ls[1:]
            continue
        # 왼쪽 | 오른쪽까지의 최소거리
        # 왼쪽 회전
        if i < len(ls) - i:
            res += i
            tmp = ls[:i]
            ls = ls[i+1:] + tmp
        # 오른쪽 회전
        else:
            res += len(ls) - i
            tmp = ls[i+1:]
            ls = tmp + ls[:i]
    print(res)

if __name__ == "__main__":
    main()