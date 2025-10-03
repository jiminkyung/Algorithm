# 수학
# 다이나믹 프로그래밍
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2502

# 첫째날, 둘째날의 떡의 갯수를 브루트포스로 탐색해서 풂.
# 🗝️피보나치의 성질을 잘 활용하면 방정식으로 간단하게 풀 수 있다. 아래에 첨부함.

# 1) 브루트포스로 푼 코드
# 메모리: 32412KB / 시간: 248ms
from sys import stdin


input = stdin.readline

def main():
    D, K = map(int, input().split())

    def calc(n1: int, n2: int) -> bool:
        dp = [0] * D
        dp[0] = n1
        dp[1] = n2

        for i in range(2, D):
            dp[i] = dp[i-1] + dp[i-2]

            # K를 초과하면 바로 False 반환
            if dp[i] > K:
                return False
        
        if dp[-1] == K:
            return True
    
    # 첫째날, 둘째날 먹은 떡의 갯수
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            if calc(i, j):
                print(i, j, sep="\n")
                return


main()


# 2) 활용 코드
# 피보나치를 좀 더 활용해서 풀 수도 있음!!!
# 출처👉 https://www.acmicpc.net/source/85389159
"""
공식을 계산해보면 아래와 같음.
Day 1 : A
Day 2 : B
Day 3 : A + B
Day 4 : (A + B) + B = A + 2B
Day 5 : (A + 2B) + (A + B) = 2A + 3B
...

즉, D번째 날의 떡 갯수는 DP[D] = [x, y]일때 x*A + y*B가 된다.
DP를 2차원 리스트로 생성, [A의 갯수, B의 갯수]형태로 저장한 뒤 계산하면 됨.
DP[4] = [DP[3][0] + DP[2][0], DP[3][1] + DP[2][1]]

그럼 DP[D]의 값으로 방정식을 만들 수 있음. -> x*A + y*B
A를 기준으로 잡고 K - x*A를 y로 나누었을때 나머지가 0이라면? (K - x*A) // y 값이 B가 되는셈.
"""
D, K = map(int, input().split())
DP = [[0, 0] for _ in range(D+1)]
DP[1] = [1, 0]
DP[2] = [0, 1]
for i in range(3, D+1) :
    DP[i] = [DP[i-1][0] + DP[i-2][0], DP[i-1][1] + DP[i-2][1]]
for i in range(1, 100001) :
    if (K - i * DP[D][0]) % DP[D][1] == 0 :
        print(i)
        print((K - i * DP[D][0]) // DP[D][1])
        break
