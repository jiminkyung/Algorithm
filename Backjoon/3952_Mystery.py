# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3952
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    P = int(input())
    test = []

    for _ in range(P):
        test.append(solve())
    
    print(*test, sep="\n")


def solve() -> str:
    # 🚨 마지막에 공백이 주어질수도 있음. 그냥 rstrip()쓰면 의미있는 공백까지 제거되어버림.
    word = input().rstrip("\n")
    N = int(input())
    X = len(word)
    nums = list(map(int, input().split()))
    curr = 0  # 현재 인덱스 (시작은 0)

    ret = [0] * N

    for i in range(N):
        curr = (curr + nums[i]) % X
        ret[i] = word[curr]
    
    return "".join(ret)


main()