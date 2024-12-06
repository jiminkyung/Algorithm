# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/7795
# 메모리: 34560KB / 시간: 128ms
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    start = cnt = 0

    for i in range(N):
        while True:
            # B의 인덱스값이 M 이상이 되거나 A가 B보다 작거나 같다면,
            # B의 인덱스값을 cnt에 더해준다. 인덱스는 0부터 시작하므로 start = 1 일때 if 조건에 걸렸다면 가능한 경우는 start = 0일때, 즉 1개가 된다.
            if start == M or A[i] <= B[start]:
                cnt += start
                break
            else:
                start += 1

    print(cnt)