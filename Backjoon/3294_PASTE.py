# 구현
# 자료 구조
# 연결 리스트


# 문제: https://www.acmicpc.net/problem/3294
# 메모리: 40768KB / 시간: 1424ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    lst = list(range(1, N+1))

    for _ in range(K):
        A, B, C = map(int, input().split())
        # 🚨잘라낸 후 남은 부분을 기준으로 C를 판단해야 함.
        section = lst[A-1:B]  # 잘라내는 부분
        remain = lst[:A-1] + lst[B:]  # 남은 부분
        lst = remain[:C] + section + remain[C:]
    
    # 10개까지만 출력
    print(*lst[:10], sep="\n")


main()