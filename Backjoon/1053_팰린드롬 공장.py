# 다이나믹 프로그래밍
# 브루트포스


# 문제: https://www.acmicpc.net/problem/1053

"""
1. 문자열의 어떤 위치에 어떤 문자를 삽입 (시작과 끝도 가능)
2. 어떤 위치에 있는 문자를 삭제
3. 어떤 위치에 있는 문자를 교환
4. 서로 다른 문자를 교환

dp[i][j] => 문자열 i부터 j까지를 팰린드롬으로 만들기 위한 연산횟수
4번 연산은 제쳐두고 1~3을 DP로 구한다.

word[i] == word[j]라면 이전 팰린드롬 값 dp[i+1][j-1]를 바로 반환해줌.

word[i] != word[j]일경우, 아래의 값에 1을 더해줌.
dp[i][j-1]: j번째 문자를 삭제하거나, j에 맞춰 i-1에 문자를 삽입하거나.
dp[i+1][j]: i번째 문자를 삭제하거나, i에 맞춰 j+1에 문자를 삽입하거나.
dp[i+1][j-1]: i에 맞춰 j를 변경 / j에 맞춰 i를 변경

    관점을 다르게 바꾸면...
    dp[i+1][j]: j에 맞춰 i에 문자 삽입. 기존 i는 i+1이 되었으므로 i+1~j 체크
    하지만 처음 관점이 더 직관적이다.

    dp[i][j]에서 i, j는 이전까지의 변형과는 상관없이 "기존 문자열을 기준으로 한 인덱스"이기 때문이다.
    다른 관점으로 생각하다보면 헷갈릴듯...?

이런식으로 DP 실행 로직을 작성한다음, 4번 연산을 브루트포스로 진행한다.
문자열을 swap 시킨 후에 DP를 실행해보고, 그 값에 1을 더해준다.
기존 최솟값과 이 값을 비교하여 갱신하는 과정을 반복한다.
"""

# ⭐1) 첫번째 풀이
# 구간별로 DP 채워넣기. Bottom-up 방식.
# 메모리: 32412KB / 288ms
from sys import stdin


input = stdin.readline
INF = float("inf")

def main():
    word = list(input().rstrip())
    N = len(word)

    dp = [[INF] * N for _ in range(N)]

    # DP 초기 셋팅
    # 길이가 1인경우 (글자 하나)는 무조건 팰린드롬이므로 연산횟수 0.
    # 길이가 2인경우는 비교 후 1 or 0으로 저장.
    for i in range(N):
        dp[i][i] = 0
    
    for i in range(N-1):
        dp[i][i+1] = int(word[i] != word[i+1])

    """
    n = 7
    길이 1일때 -> i는 0부터 5까지
    길이 2일때 -> i는 0부터 (i+2) < 7 => i < n - 길이
    """

    def dynamic() -> int:
        for length in range(2, N):  # 구간 길이
            for i in range(N - length):
                j = i + length

                if word[i] == word[j]:  # 글자 i, j가 같다면 i-j 사이의 값들을 그대로 사용
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1], dp[i+1][j-1]) + 1

        return dp[0][N-1]
    

    min_cnt = dynamic()

    # 4번 조건 고려하기
    for i in range(N):
        for j in range(i+1, N):
            if word[i] != word[j]:
                word[i], word[j] = word[j], word[i]
                min_cnt = min(min_cnt, dynamic()+1)
                word[i], word[j] = word[j], word[i]
    
    print(min_cnt)


main()


# 2) 재귀로 DP 채워넣기. Top-down 방식.
# 이건 다른 사람의 풀이를 보고 작성해봄.
# 👉 https://rapun7el.tistory.com/312
# 메모리: 32412KB / 시간: 1252ms
from sys import stdin


input = stdin.readline
INF = float("inf")

def main():
    word = list(input().rstrip())
    N = len(word)

    def dynamic():
        dp = [[INF] * N for _ in range(N)]

        def dfs(start, end, dp):
            if dp[start][end] != INF:
                return dp[start][end]

            if start >= end:
                return 0

            for i, j in ((1, 0), (0, -1), (1, -1)):
                dp[start][end] = min(dp[start][end], dfs(start+i, end+j, dp) + int((i, j) != (1, -1) or word[start] != word[end]))
            return dp[start][end]
        
        return dfs(0, N-1, dp)
    
    min_cnt = dynamic()
    
    # 4번 조건 고려하기
    for i in range(N-1):
        for j in range(i+1, N):
            if word[i] != word[j]:
                word[i], word[j] = word[j], word[i]
                min_cnt = min(min_cnt, dynamic()+1)
                word[i], word[j] = word[j], word[i]
    
    print(min_cnt)


main()