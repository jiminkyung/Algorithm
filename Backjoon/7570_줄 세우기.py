# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/7570

# LIS 문제다. 답이 "N - 증가하는 부분의 길이"인건 알아차렸지만 LIS와 직결시키지 못했다;;
# => 굳이 LIS를 구하는 방식을 사용하지 않아도 됐었다. 방식을 그대로 사용하면 시간초과다.

# 참고한 풀이👉 https://velog.io/@ttc1018/%EB%B0%B1%EC%A4%80-7570-%EC%A4%84-%EC%84%B8%EC%9A%B0%EA%B8%B0-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DP
# => 하지만 매 순회마다 최대길이값을 갱신해주는걸로 수정해야함.
# => 관련 반례는 https://www.acmicpc.net/board/view/148840

# 메모리: 132864KB / 시간: 792ms
from sys import stdin


input = stdin.readline

N = int(input())
line = list(map(int, input().split()))

idx = [0] * (N+1)

for i, child in enumerate(line):
    idx[child] = i

max_cnt = 0
cnt = 1

for i in range(1, N):
    if idx[i] < idx[i+1]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(cnt, max_cnt)

print(N - max_cnt if N != 1 else 0)