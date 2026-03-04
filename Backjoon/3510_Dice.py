# 수학
# 그리디 알고리즘
# 정렬
# 확률론


# 문제: https://www.acmicpc.net/problem/3510
# 메모리: 36504KB / 시간: 76ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())
    # 기대값 = 각 주사위의 (면에 적힌 수의 합) / 면의 수
    # 그러니까 면의 수가 적은 주사위에 큰 수를 배치해야함.

    # (면의 수, 순서) 형태로 저장 후 오름차순으로 정렬.
    a = [(d, i) for i, d in enumerate(map(int, input().split()))]
    a.sort()
    num = sum(d for d, _ in a)  # 면의 수를 모두 더한 값부터 1까지 순차적으로 지정해줘야함.

    # ret[i]: i번째 주사위에 들어갈 숫자들
    ret = [[] for _ in range(n)]

    for d, i in a:
        for _ in range(d):
            ret[i].append(num)
            num -= 1
    
    # 기댓값
    E = 0.0

    for line in ret:
        E += sum(line) / len(line)
    
    print(f"{E:.5f}")

    for line in ret:
        print(*line)


main()