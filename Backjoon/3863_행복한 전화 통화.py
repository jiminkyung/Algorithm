# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3863
# 메모리: 40892KB / 시간: 348ms
from sys import stdin


def main():
    data = stdin.read().splitlines()[:-1]

    idx = 0
    while idx < len(data):
        N, M = map(int, data[idx].split())
        idx += 1
        calling = []

        # Source, Destination, Start, Duration
        # 사실상 Source, Destination은 필요 X
        for _ in range(N):
            _, _, start, duration = map(int, data[idx].split())
            calling.append((start, duration + start))
            idx += 1
        
        ret = []

        for _ in range(M):
            start, duration = map(int, data[idx].split())
            duration += start
            cnt = 0
            
            # (s, d)일때 실제 통화 시간은 s ~ d-1임. 즉 [s, d)인 셈인데...
            # 어차피 통화내역 데이터로 주어진 값도 [s, d), 구간 데이터로 주어진 값도 [s, d) 형태이므로 상관 X
            for s, d in calling:
                # 조건 만족 시 겹치는것으로 판단.
                if s < duration and start < d:
                    cnt += 1
            
            ret.append(cnt)
            idx += 1
        
        print(*ret, sep="\n")


main()