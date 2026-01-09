# 그래프 이론
# 브루트포스 알고리즘
# 그래트 탐색


# 문제: https://www.acmicpc.net/problem/3182
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # numbers[i]: i번째 선배가 추천한 선배 번호
    numbers = [0] + [int(input()) for _ in range(N)]

    max_cnt = 1
    max_num = -1

    for num in range(1, N+1):
        visited = [False] * (N+1)
        curr = num
        visited[curr] = True
        cnt = 1

        # 이미 확인한 선배가 나올때까지 파도타기 진행
        while True:
            nxt = numbers[curr]

            if visited[nxt]:
                break

            visited[nxt] = True
            cnt += 1
            curr = nxt
        
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = num
    
    print(max_num)


main()