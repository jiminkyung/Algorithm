# 문제집 - 0x0B - 재귀


# 문제: https://www.acmicpc.net/problem/2448

# 어려워서 다른 풀이들을 참고했다... 재귀는 연습이 더 필요할듯하다.
# 참고👉 https://lcyking.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2448%EB%B2%88-%EB%B3%84-%EC%B0%8D%EA%B8%B0-11

# 메모리: 178044KB / 시간: 808ms
from sys import stdin


N = int(stdin.readline())
star = [[" "] * 2*N for _ in range(N)]

def make_star(x, y, n):
    if n == 3:
        for i in range(3):
            for j in range(i+1):
                star[x+i][y+j] = star[x+i][y-j] = "*"
        star[x+1][y] = " "
        return
    
    m = n // 2
    make_star(x, y, m)
    make_star(x+m, y-m, m)
    make_star(x+m, y+m, m)

make_star(0, N-1, N)

for line in star:
    print("".join(line))