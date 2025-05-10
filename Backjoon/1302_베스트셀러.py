# 정렬
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/1302
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    books = {}

    # {책 제목: 팔린 갯수} 형태로 저장
    for _ in range(N):
        title = input().rstrip()
        books[title] = books.get(title, 0) + 1
    
    # 1️⃣책이 많이 팔린 순, 2️⃣책 제목 순으로 정렬
    sorted_books = sorted(books.keys(), key=lambda x: (-books[x], x))
    print(sorted_books[0])


main()