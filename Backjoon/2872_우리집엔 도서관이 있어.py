# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2872
# 메모리: 45192KB / 시간: 112ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    books = [int(input()) for _ in range(N)]
    num = N
    
    # 뺀 책은 맨 위에 쌓아야 함.
    # 아래에서부터 이미 정렬된 연속된 구간을 찾아나가면 됨.
    # N, N-1, N-2... 순서로 체크하면서, 책 번호가 일치한다면 이미 올바른 위치에 있는것임.
    for i in range(N-1, -1, -1):
        if books[i] == num:
            num -= 1
    
    # 남은 num 값 = 위로 올려야 하는 책의 수
    print(num)


main()