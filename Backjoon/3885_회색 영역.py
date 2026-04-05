# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/3885
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    data = stdin.read().splitlines()[:-1]

    idx = 0
    while idx < len(data):
        n, w = map(int, data[idx].split())
        idx += 1

        # 주어지는 값들이 어느 구간에 속하는지 카운트. 비율이 곧 높이가 되는 형태임.
        # 예를들어 0~9에 해당되는 값이 3개, 10~19에 해당되는 값이 5개라면, 기준 높이는 5가 됨.
        # 그럼 0~9 구간의 높이는 3 / 5 가 되는 셈.
        values = list(map(int, data[idx:idx+n]))
        idx += n
        size = (max(values) // w) + 1

        # cnt[x]: [w*x, 2w*x) 구간에 해당되는 값들의 갯수
        cnt = [0] * size

        for val in values:
            cnt[val // w] += 1
        
        # 가장 많은 비율을 차지하는 구간이 기준 높이가 됨.
        max_cnt = max(cnt)

        ret = 0.01

        for i in range(size):
            height = cnt[i] / max_cnt
            # 색상은 그래프 기준 맨 왼쪽은 1, 맨 오른쪽은 0임. k/k, k-1/k, k-2/k... 0 형식으로 변화.
            color = (size - 1 - i) / (size - 1)
            ret += height * color
        
        print(ret)


main()