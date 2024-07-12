# 동적 계획법 1

# AI선생님의 도움을 받은 풀이
# 메모리: 31120KB / 시간: 32ms

from sys import stdin


input = stdin.readline
N = int(input().strip())
stairs = [int(input().strip()) for _ in range(N)]

def upstairing():
    if N <= 2:
        return sum(stairs)
    
    # dp를 따로 만들어줘야한다. "연속된 세 개의 계단을 모두 밟을수는 없음" 조건 때문임.
    dp = [0] * N

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, N):
        # dp[i-1]에는 i-2번째 혹은 i-3번째 계단의 점수가 포함되어 있음.
        # 만약 dp[i-1]가 i-2번째를 선택한 상태라면 위의 조건👆을 만족하지 못하게 됨. => 따라서 stairs의 실제 값을 참조해야함.
        dp[i] = max(dp[i-2], dp[i-3]+stairs[i-1]) + stairs[i]
    
    return dp[-1]

print(upstairing())