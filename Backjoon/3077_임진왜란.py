# 자료 구조
# 브루트포스 알고리즘
# 집합과 맵
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3077
# 메모리: 33432KB / 시간: 252ms
from sys import stdin
from itertools import combinations


input = stdin.readline

def main():
    N = int(input())

    # 답을 0부터 N-1까지 숫자로 맵핑
    answer = {name: i for i, name in enumerate(input().rstrip().split())}
    data = [answer[d] for d in input().rstrip().split()]

    total = N * (N-1) // 2
    cnt = 0

    for comb in combinations(data, 2):
        if comb[0] < comb[1]:
            cnt += 1
    
    print(f"{cnt}/{total}")


main()