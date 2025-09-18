# 구현


# 문제: https://www.acmicpc.net/problem/2238
# 메모리: 41624KB / 시간: 104ms
from sys import stdin


input = stdin.readline

def main():
    # U: 금액의 상한, N: 경매에 참여한 횟수
    U, N = map(int, input().split())
    lst = {}

    for _ in range(N):
        S, P = input().split()
        # lst[P]: P 금액으로 참여한 경매자들
        lst.setdefault(int(P), []).append(S)
    
    # 경매자 수가 가장 적은 순, 낮은 가격순으로 오름차순 정렬
    order = sorted(lst, key=lambda x: (len(lst[x]), x))
    print(lst[order[0]][0], order[0])


main()