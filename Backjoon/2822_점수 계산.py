# 정렬


# 문제: https://www.acmicpc.net/problem/2822
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # (점수, 문제 번호) 형태로 저장 후 내림차순 정렬
    score = [(s, i) for i, s in enumerate([int(input()) for _ in range(8)], start=1)]
    score.sort(reverse=True)

    # 가장 높은 점수 5개를 점수, 번호 형태로 다시 뽑아냄
    point, num = map(list, zip(*score[:5]))
    print(sum(point))
    print(*sorted(num))


main()