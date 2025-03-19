# 브루트포스


# 문제: https://www.acmicpc.net/problem/1027

# 기울기 문제. 본인 왼쪽/오른쪽 모두 체크해야함.

# 왼쪽/오른쪽 나눠서 두번 체크하지 않고 한번에 체크할 수 있음...
# 참고👉 https://magentino.tistory.com/356

# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    heights = list(map(int, input().split()))
    count = [0] * N  # count[x]: x건물에서 보이는 건물의 수

    for i in range(N-1):
        max_slope = float("-inf")
        for j in range(i+1, N):
            slope = (heights[j] - heights[i]) / (j - i)
            if slope <= max_slope:  # 현재 기울기가 이전 기울기보다 커야함
                continue
            max_slope = slope
            count[i] += 1
            count[j] += 1  # i -> j가 보인다면 j -> i도 보임

    print(max(count))


main()