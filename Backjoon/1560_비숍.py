# 애드 훅


# 문제: https://www.acmicpc.net/problem/1560
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # 비숍은 대각선으로만 움직일 수 있음.
    # 흑->흑, 백->백 으로만 이동 가능... 즉 흑칸에 나란히, 바로 옆 백칸에 나란히 놓으면?

    # print((N+1)//2 * 2) => ❌ 뭔가 이상해서 다른 풀이를 찾아 봄.
    # 🚨↘↗ 와 같은 이동은 고려할필요 X. 첫 이동 방향만 고려해주면 됨.
    # 참고👉 https://making-trouble.tistory.com/7

    print((N-1)*2 if N > 1 else 1)


main()