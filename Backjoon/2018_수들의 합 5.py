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
a부터 시작하는 k개의 연속된 자연수 a, a+1, a+2, ..., a+k-1를 생각해보자.
- 합 = k*a + k*(k-1)/2 = N (a만 떼어냄)
- a = (N - k*(k-1)/2) / k
- a가 자연수가 되려면 (N - k*(k-1)/2) = (0+1...k-1)가 k로 나누어 떨어져야 함

예시) N=15인 경우:
- k=1: a=15 → 15 (가능)
- k=2: a=7 → 7+8=15 (가능) 
- k=3: a=4 → 4+5+6=15 (가능)
- k=4: a=2.25 → 불가능 (자연수 아님)
- k=5: a=1 → 1+2+3+4+5=15 (가능)
    => 총 4가지

아래 코드에서 p = k로 생각하면 됨.
p개의 연속된 숫자의 합이 n이 되는 경우는, 각 p당 한개씩밖에 없음. 고로 아래처럼 푸는게 훨 효율적임.
"""
n = int(input())

ans = 0
p = 1
s = 1
while s <= n:
    if not (n - s) % p:
        ans += 1
    p += 1
    s += p
print(ans)
