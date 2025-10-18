# 수학
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2622

# a*b로 풀면 시간초과다. 식을 사용해서 풀어야 함.
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    cnt = 0

    # 변 a, b, c가 있고 c가 가장 긴 변이라고 했을때,
    # 길이는 a <= b <= c 여야 함.
    # 따라서 a의 가용범위는 1 ~ N//3
    for a in range(1, N//3 + 1):
        # 이제 b의 최댓값과 최솟값을 구해서 가능한 갯수를 구해줄거임.
        # b의 최댓값은 (N - a) // 2 (아래의 식)
            # c = N - a - b
            # b <= N - a - b
            # 2b <= N - a
            # b <= (N - a) // 2
        b_max = (N - a) // 2

        # b의 최솟값은 a 또는 N//2 - a + 1 (아래의 식)
            # a + b > c 여야함.
            # a + b > N - a - b 이고, 2b > N - 2a니까 b > N/2 - a
        b_min = max(a, N//2 - a + 1)  # 둘 중 더 작은값을 최솟값으로 지정
        
        # (a <= b <= c)와 (a + b < c)모두 만족하는 b의 범위는 b_max ~ b_min
        # 구간 갯수가 곧 "제일 작은 변 a가 정해져있을때 가능한 (b, c)의 갯수"가 됨.
        cnt += b_max - b_min + 1
    
    print(cnt)


main()