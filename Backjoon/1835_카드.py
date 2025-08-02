# 구현
# 시뮬레이션
# 자료구조  # 덱


# 문제: https://www.acmicpc.net/problem/1835

# 1) 계산 버전
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    queue = [N]

    for i in range(N-1, 0, -1):
        queue = [i] + queue
        # 4 3 2 1 -> 1 4 3 2 로 바뀌었다면, 3번 바꾼 셈.
        # 3 % 4 = 3, 4 - 3 = 1 이니까 queue[1:] + queue[:1]을 하면 4 3 2 1 이었다는걸 알 수 있음.
        # 만약 4 3 -> 3 4 로 바뀌었고, 이게 3번 바꾼것이라면?
        # 3 % 2 = 1, 2 - 1 = 1 이니까 queue[1:] + queue[:1]을 하면 4 3 이었다는걸 알 수 있다.
        idx = len(queue) - i % len(queue)
        queue = queue[idx:] + queue[:idx]
    
    print(*queue)


main()


# 2) deque 사용 버전
# 메모리: 34908KB / 시간: 84ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    N = int(input())
    queue = deque([N])

    for i in range(N-1, 0, -1):
        # 숫자 추가 후 반대로 처리 (뒤에서 뺀 값을 앞에 추가)
        queue.appendleft(i)
        for _ in range(i):
            prev = queue.pop()
            queue.appendleft(prev)
    
    print(*queue)


main()