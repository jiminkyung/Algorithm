# 구현
# 자료 구조
# 큐


# 문제: https://www.acmicpc.net/problem/2161

# 처음엔 수학으로 풀 수 있을줄 알았다만... 정직하게 덱으로 풀어야 함 ㅜㅜ

# 수학으로 푼 방식은 다음과 같음.
# 마지막 남은 카드는 N - int(N % 2) -> N이 짝수면 N 그대로, 홀수면 N-1.
# 1부터 N까지의 모든 홀수를 ret에 추가. 그리고 N보다 작은 짝수를 내림차순으로 추가. 마지막에 위에서 구한 마지막 카드 추가.
# 어쨌든 위 방법은 안됨.

# 메모리: 34900KB / 시간: 64ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    N = int(input())

    queue = deque(range(1, N+1))
    ret = []
    
    while queue:
        top = queue.popleft()
        ret.append(top)

        queue.rotate(-1)
    
    print(*ret)


main()