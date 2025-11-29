# 그리디 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/2865
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    total = []
    N, M, K = map(int, input().split())

    for _ in range(M):
        data = input().rstrip().split()
        # (능력치, 번호) 형태로 저장
        total.extend([(float(data[i+1]), int(data[i])-1)for i in range(0, N*2, 2)])
    
    # 내림차순으로 정렬
    total.sort(reverse=True)
    used = [False] * N  # 진출 확정 여부
    ret = 0.0

    # 장르가 겹쳐도 상관은 없으니 점수가 높은 순서대로 한명씩 뽑음.
    # 이미 뽑힌 사람이면 불가. K명을 다 뽑으면 마감.
    for score, num in total:
        if used[num]:
            continue

        ret += score
        used[num] = True
        K -= 1

        if not K:
            break
    
    print(f"{ret:.1f}")


main()