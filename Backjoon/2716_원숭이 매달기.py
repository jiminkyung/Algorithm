# 자료구조
# 트리
# 스택


# 문제: https://www.acmicpc.net/problem/2716
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # 왼쪽 원숭이 수 == 오른쪽 원숭이 수 여야 함.
    # 각 분기마다 왼 == 오 조건을 만족시켜야 하므로, 해당 분기에서 필요한 원숭이 수 = (왼)*2 거나 (오)*2 가 됨.

    # 이진트리 특성상 깊이 X의 노드 갯수 = 2^X 임.
    # -> 가장 깊은 곳을 기준으로 밸런스를 맞추면 됨.
    # 🗝️ 따라서 트리의 최대 깊이를 구하고, 2^(최대깊이) 를 해준값이 답이 된다.
    T = int(input())

    for _ in range(T):
        data = input().rstrip()

        if not data:
            print(1)
            continue

        stack = []
        max_degree = 0

        for d in data:
            if d == "[":
                stack.append(1)
            else:
                degree = len(stack)
                stack.pop()
                max_degree = max(max_degree, degree)
        
        print(2**max_degree)


main()