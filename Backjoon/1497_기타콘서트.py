# 조합론
# 비트마스킹
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1497
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    guitars = [0] * N

    # guitars[x]: x번째 기타가 연주할 수 있는 곡 상태. 비트로 표현함.
    for i in range(N):
        _, available = input().rstrip().split()
        for j, a in enumerate(available):
            if a == "Y":
                guitars[i] |= 1 << j

    max_songs = 0
    min_cnt = N + 1

    # 기타 선택 조합을 하나씩 체크
    for comb in range(1, 1 << N):
        cnt = bit = 0  # cnt: 선택한 기타 수, bit: 선택한 기타로 연주할 수 있는 곡들
        for i in range(N):
            # 만약 현재 기타가 해당 조합에 포함되어있는 상태라면,
            if comb & (1 << i):
                bit |= guitars[i]  # 연주 가능한 곡 리스트를 갱신
                cnt += 1
        songs = bin(bit).count("1")

        if songs > max_songs:
            max_songs = songs
            min_cnt = cnt
        elif songs == max_songs:  # 연주할 수 있는 곡 수가 같다면, 선택한 기타 수가 더 적은 경우를 채택함
            min_cnt = min(min_cnt, cnt)
    
    # 🚨처음에는 min_cnt < N+1로 체크했지만 틀림.
    # => max_songs가 0이어도 min_cnt가 < N+1을 만족할 수 있음. songs == max_songs 조건 때문.
    # 따라서 기타 갯수가 아닌 곡의 갯수를 기준으로 체크해야 함.
    print(min_cnt if max_songs > 0 else -1)


main()