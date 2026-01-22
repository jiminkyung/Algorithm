# 구현


# 문제: https://www.acmicpc.net/problem/3230
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    # 기존 1위였던 사람은 새로운 1위가 등장하면 2위로 밀려나는 방식.
    first = []

    for i in range(N):
        num = int(input())

        # 본인이 들어가야 할 등수 앞에 그 이상의 사람이 있다면, 끼어들기.
        if len(first) >= num:
            first = first[:num-1] + [i+1] + first[num-1:]
        else:  # 아니라면 그냥 뒤에 추가.
            first.append(i+1)
    
    # 새로운 데이터가 M등부터 1등 순서로 주어진다 했으므로, 이에 맞춰 뒤집어줌.
    first = first[:M][::-1]
    second = []

    for idx in first:
        num = int(input())

        if len(second) >= num:
            second = second[:num-1] + [idx] + second[num-1:]
        else:
            second.append(idx)
    
    print(*second[:3], sep="\n")


main()