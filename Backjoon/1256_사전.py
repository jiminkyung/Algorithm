# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1256

# 조합만 생각하고 풀다가 막혔다. 결국 다른 풀이로 이해함.
# 참고👉 https://hillier.tistory.com/81
# 나중에 다시 한 번 풀어봐야할 문제... DP

# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M, K = map(int, input().split())

    # dp[i][j]: 'a'를 i개, 'z'를 j개 사용하여 만들 수 있는 문자열 갯수
    # 'a'나 'z' 중 하나만 사용하는 경우 문자열은 단 1개만 가능하므로 1로 초기화
    dp = [[1] * (M+1) for _ in range(N+1)]

    # dp값 채워넣기
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # => 첫 글자가 'a'인 경우(dp[i-1][j])와 첫 글자가 'z'인 경우(dp[i][j-1])의 합
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # 만들 수 있는 문자열의 총 갯수가 K개보다 적으면 -1 출력
    if dp[N][M] < K:
        print(-1)
        return
    
    ret = ""
    while True:
        # 남은 'a'나 'z'가 없으면 남은 'a' or 'z'를 모두 추가하고 종료
        if N == 0 or M == 0:
            ret += "z" * M  # 남은 'z' 모두 추가 ('a'가 없을경우)
            ret += "a" * N  # 남은 'a' 모두 추가 ('z'가 없을경우)
            break

        # 첫 글자를 'a'로 선택했을때 가능한 문자열 갯수
        s = dp[N-1][M]

        # K가 s 이하라면, 첫 글자로 'a' 선택 (사전순이므로)
        if K <= s:
            ret += "a"
            N -= 1
        # K가 s보다 크면 첫 글자로 'z' 선택
        else:
            ret += "z"
            # ex) N=2, M=2, K=6일때, 'a'로 시작하는 경우는 3개 (dp[1][2] = 3)
            # => 'a'로 시작하는 경우를 건너뛰었으므로 K에서 빼줌
            # => K = 6-3 = 3, (남은 문자열 중에서 3번째를 찾아야 함)
            K -= s  # 건너뛴 문자열 갯수만큼 조정
            M -= 1
    
    print(ret)


main()