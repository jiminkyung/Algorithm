# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2232

# 다른 코드를 참고한 풀이다...
# 메모리: 36064KB / 시간: 68ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    bomb = [0] + [int(input()) for _ in range(N)] + [0]

    ret = []
    # 🚨Pi를 "초과"하는 힘을 받아야지만 폭파된다. 즉, [6, 6]인 상태에서 어느 한 쪽이 터져도 다른 한쪽은 영향이 없다.
    # 왼쪽에서부터 탐색한다. 만약 현재 지뢰가 양쪽 지뢰보다 크거나, 어느 한쪽과 같다면 터뜨려야함.
    for i in range(1, N+1):
        if bomb[i-1] <= bomb[i] >= bomb[i+1]:
            ret.append(i)
    
    print(*ret, sep="\n")


main()