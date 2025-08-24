# 수학
# 두 포인터


# 문제: https://www.acmicpc.net/problem/2018

# 수학적으로 풀면 훨씬 간단하고 빠른 문제다. 아래 참고.
# 메모리: 32412KB / 시간: 1292ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    
    if N == 1:
        print(1)
        return

    left = right = 1
    curr = 1
    cnt = 0

    # 오른쪽 포인터가 N의 절반값 이하일때까지만
    while right <= (N+1) // 2:
        # 현재 sum이 N보다 작다면 오른쪽 포인터 이동, curr 증가
        if curr < N:
            right += 1
            curr += right
        # N보다 크다면 curr 감소 후 왼쪽 포인터 이동
        elif curr > N:
            curr -= left
            left += 1
        # N이라면 카운트 후 curr 감소, 왼쪽 포인터 이동
        else:
            cnt += 1
            curr -= left
            left += 1
    
    # 자기 자신(N)도 경우의 수에 포함되므로 +1 처리 (단, N = 1일경우엔 X)
    print(cnt + 1)


main()


# ⭐굳이 투포인터로 풀지 않아도 됨.
# 정답 코드들을 보니 실행시간이 32ms길래 확인해봤다...
# 관련 글👉 https://www.acmicpc.net/board/view/94551
"""
a부터 시작하는 m개의 연속된 자연수 a, a+1, a+2, ..., a+m-1를 생각해보자.
-> 위 식에서 a만 따로 떼어내면, 합 = a*m + m(m-1)/2 = N
-> 이를 a에 대해 정리하면 a = (n - m(m-1)/2) / m
    => 따라서 (n - m(m-1)/2)가 m의 배수이면 시작점 a가 자연수로 존재한다.

예시) N=15인 경우:
- m=1: a=15 → 15 (가능)
- m=2: a=7 → 7+8=15 (가능) 
- m=3: a=4 → 4+5+6=15 (가능)
- m=4: a=2.25 → 불가능 (자연수 아님)
- m=5: a=1 → 1+2+3+4+5=15 (가능)
    => 총 4가지
"""
n = int(input())

ans = 0
p = 1
s = 1
# m(=p)를 1부터 증가시키며, 1+2+...+m = m(m+1)/2 값을 s로 관리한다.
# (n - s)가 p로 나누어떨어지는지 확인하여 조건을 만족하면 경우의 수를 증가.
while s <= n:
    if not (n - s) % p:
        ans += 1
    p += 1
    s += p
print(ans)
