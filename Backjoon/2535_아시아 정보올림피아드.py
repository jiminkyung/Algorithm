# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/2535
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x: -x[2])  # 점수 기준으로 정렬

    # cnt[x]: x나라에서 획득한 메달 수
    cnt = [0] * (N+1)
    total = 0

    for i, num, score in scores:
        if cnt[i] == 2:
            continue

        cnt[i] += 1
        total += 1
        print(i, num)

        # 금은동 모두 수여했으면 break
        if total == 3:
            break


main()