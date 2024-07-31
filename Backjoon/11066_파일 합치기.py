# 동적 계획법 2

"""
Python3로 통과하기 위해선 크누스 알고리즘(Knuth's Algorithm)을 사용해야함.
아래는 Python3로 통과하지 못한 코드들.
나중에 다시 봐야할 문제다.
"""

# 1
from sys import stdin


input = stdin.readline
T = int(input())

def min_cost(K, arr):
    pre_sum = [0] * (K+1)
    for i in range(1, K+1):
        pre_sum[i] = pre_sum[i-1] + arr[i-1]

    dp = [[0]*K for _ in range(K)]

    for length in range(2, K+1):
        for i in range(K-length+1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + pre_sum[j+1] - pre_sum[i]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][K-1]

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    print(min_cost(K, files))


# 2, 참고: https://supersfel.tistory.com/entry/11066%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%84%A4%EB%AA%85%EC%9C%84%EC%A3%BC
from sys import stdin


input = stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))

    pre_sum = [0] * (K+1)
    for i in range(1, K+1):
        pre_sum[i] = pre_sum[i-1] + arr[i-1]
    
    dp = [[0]*(K+1) for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) +(pre_sum[j+i-1] - pre_sum[j-1])
    
    print(dp[1][K])


# Python3로 통과된 코드들.

# 48ms
def solution():
    stdin = open(0, "rb")
    T = int(stdin.readline())  # 테스트 케이스의 수를 입력받음
    for _ in range(T):
        K = int(stdin.readline())  # 각 테스트 케이스의 파일 수를 입력받음
        sizes = list(map(int, stdin.readline().split()))  # 파일 크기들을 리스트로 입력받음

        ans = 0  # 총 비용을 저장할 변수
        cursor = 1  # 현재 처리 중인 위치를 나타내는 커서
        q = [1_000_000_000, sizes[0]] + [0] * K  # 파일 크기를 저장할 리스트. 맨 앞에 큰 값을 넣어 경계 조건 처리

        def combine(end):
            nonlocal ans, cursor
            cost = q[end-1] + q[end]  # 두 파일을 합치는 비용 계산
            ans += cost  # 총 비용에 더함

            q.pop(end)  # 합친 파일 중 하나를 제거
            
            # 합친 파일의 크기를 적절한 위치에 삽입
            i = end-2
            while q[i] < cost:
                i -= 1
            q[i+2:end] = q[i+1:end-1]
            q[i+1] = cost

            cursor -= 1  # 커서 위치 조정
            # 필요한 경우 추가로 파일들을 합침
            while i > 0 and q[i-1] <= cost:
                d = cursor-i
                combine(i)
                i = cursor-d

        for x in sizes[1:]:  # 첫 번째 파일을 제외한 나머지 파일들에 대해
            while q[cursor-1] <= x:  # 현재 파일보다 작거나 같은 파일들을 모두 합침
                combine(cursor)
            cursor += 1
            q[cursor] = x  # 현재 파일을 리스트에 추가

        while cursor > 1:  # 남은 파일들을 모두 합침
            combine(cursor)
        
        print(ans)  # 최종 비용 출력

solution()

# 792ms
from sys import stdin

def sol2(n: int, lst: list) -> int:
    # dp[i][j]: i부터 j까지의 파일을 합치는 최소 비용
    dp = [[0]*n for _ in range(n)]
    
    # sum_dp[i]: 0부터 i-1까지의 파일 크기의 누적 합
    sum_dp = [0]
    
    # knuth[i][j]: dp[i][j]를 계산할 때의 최적 분할 지점
    knuth = [[0]*n for _ in range(n)]
    
    # 초기화: 각 파일 자체의 비용과 누적 합 계산
    for i in range(n):
        knuth[i][i] = i
        sum_dp.append(sum_dp[-1]+lst[i])
    
    # 구간의 길이를 1부터 n-1까지 증가시키며 dp 테이블 채우기
    for i in range(1, n):
        for j in range(n-i):
            min_value = float('inf')
            # Knuth's Optimization: 이전에 계산된 최적 분할 지점을 이용해 탐색 범위 좁히기
            for k in range(knuth[j][j+i-1], min(knuth[j+1][j+i]+1, j+i)):
                x = dp[j][k] + dp[k+1][j+i]
                if x < min_value:
                    min_value = x
                    knuth[j][j+i] = k
            # 최소 비용 계산: 좌우 부분의 최소 비용 + 현재 구간의 합
            dp[j][j+i] = min_value + sum_dp[j+i+1] - sum_dp[j]
    
    # 전체 구간(0부터 n-1까지)의 최소 비용 반환
    return dp[0][n-1]

# 입력 처리 및 결과 출력
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    lst = [*map(int, stdin.readline().split())]
    print(sol2(N, lst))