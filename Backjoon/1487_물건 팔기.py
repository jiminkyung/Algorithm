# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1487
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort()  # 가격 기준으로 오름차순 정렬

    max_money = max_cost = 0

    for i in range(N):
        cost = lst[i][0]
        money = 0
        # cost 가격으로 팔 수 있는 사람들만 체크
        for j in range(i, N):
            curr = cost - lst[j][1]
            # 파는게 손해라면 안 팜
            if curr > 0:
                money += curr
        
        if money > max_money:
            max_money = money
            max_cost = cost
    
    print(max_cost)


main()