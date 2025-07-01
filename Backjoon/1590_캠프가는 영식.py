# 브루트포스 알고리즘
# 이분 탐색


# 문제: https://www.acmicpc.net/problem/1590

# 확인해보니 이분탐색으로도 분류되어 있는 문제. 아마 기다리는시간 x를 기준으로 진행하는듯?ㄴ
# 버스 수가 최대 50대이므로 브루트포스로 체크하는게 빠름.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # N: 버스 갯수, T: 버정에 도착한 시간
    N, T = map(int, input().split())
    min_diff = int(1e9)

    for _ in range(N):
        # S: 첫차시간, I: 간격, C: 최대 운행횟수
        S, I, C = map(int, input().split())

        # 버정 도착 이후에 오는 첫차 찾기
        while S < T and C > 1:
            S += I
            C -= 1
        
        # 버스를 탈 수 있다면 기다리는 시간 계산
        if 0 <= S - T < min_diff:
            min_diff = S - T
            if min_diff == 0:
                break
    
    print(min_diff if min_diff != int(1e9) else -1)


main()