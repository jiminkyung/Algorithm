# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2012

# 질문 게시판에 이런 글이 있었음👉 https://www.acmicpc.net/board/view/123023
# 반례는 [1, 1, 4, 4] 같은 경우가 있겠다. 불만도는 개별로 계산해야함.

# 메모리: 54820KB / 시간: 368ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    # 실제 순위도 오름차순으로 진행되므로 작은값끼리/큰값끼리 매칭시키는게 제일 효율적임
    lst.sort()  # 예상 등수를 오름차순으로 정렬

    ret = 0

    # |실제 순위 - 예상 순위| 값 계산
    for i, s in enumerate(lst, start=1):
        ret += abs(i - s)
    
    print(ret)


main()