# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3213
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    pizza = [0, 0, 0, 0]

    for _ in range(N):
        data = input().rstrip()

        if data == "1/2":
            pizza[2] += 1
        elif data == "1/4":
            pizza[1] += 1
        else:
            pizza[3] += 1
    
    cnt = 0
    p1, p3 = pizza[1], pizza[3]
    # 1/4 + 3/4 = 1 이므로 피자 한판 가능.
    if p1 == p3:
        cnt += p1
        p1 = 0
    # 1/4는 1/2와 공존 가능. 둘이 합쳐 피자 한판.
    elif p1 > p3:
        cnt += p3
        p1 -= p3
    # 3/4은 1/2와 공존 불가능. 만족시키기 위해선 피자 한 판을 통째로 대령해야함.
    elif p1 < p3:
        cnt += p3
        p1 = 0
    
    # 일단 1/2 피자 먼저 처리,
    p2 = pizza[2]
    cnt += p2 // 2
    p2 %= 2

    # 남았다면 한판일것임. 처리하는데, 만약 1/4 피자가 남았다면 묶어서 처리.
    if p2:
        cnt += 1
        p2 = 0
        if p1:
            p1 -= 1
    
    # 1/4 피자는 4개에 한판 가능.
    cnt += (p1 + 3) // 4
    
    print(cnt)


main()