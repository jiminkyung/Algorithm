# 구현
# 자료 구조
# 브루트포스 알고리즘
# 스택


# 문제: https://www.acmicpc.net/problem/2304

# 스택으로도 분류되어 있는 문제지만 굳이 필요하진 않음.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # 제일 높은 막대를 중심으로 왼쪽 구간, 오른쪽 구간을 나눌거임.
    # 일단 x좌표 순서대로 정렬
    pillar = [tuple(map(int, input().split())) for _ in range(N)]
    pillar.sort()

    # 그리고 제일 높은 막대와 해당 막대의 인덱스를 저장한다.
    heights = [(-pillar[i][1], i) for i in range(N)]
    max_height, max_idx = min(heights)
    max_height *= -1  # -높이로 정렬했으므로 원상복구
    # 제일 큰 막대의 면적은 높이 * 1 이므로 미리 저장
    ret = max_height

    # 왼쪽 구간 계산
    # 높이: 현재까지의 높이 중 가장 높은값 / 너비: 다음 막대까지의 거리
    # -> 이 둘을 곱해준 값이 면적
    curr = 0
    for i in range(max_idx):
        x, height = pillar[i]
        curr = max(curr, height)

        ret += curr * (pillar[i+1][0] - x)
    
    # 오른쪽 구간 계산
    # 왼쪽과 같은 로직으로 계산, BUT 오른쪽부터 시작해서 중간까지 나아가는 방식.
    curr = 0
    for i in range(N-1, max_idx, -1):
        x, height = pillar[i]
        curr = max(curr, height)

        ret += curr * (x - pillar[i-1][0])
    
    print(ret)


main()