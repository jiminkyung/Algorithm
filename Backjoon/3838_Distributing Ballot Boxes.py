# 구현
# 이분 탐색
# 매개 변수 탐색


# 문제: https://www.acmicpc.net/problem/3838
# 메모리: 138032KB / 시간: 3272ms
from sys import stdin


def main():
    data = stdin.read().splitlines()
    idx = 0

    while idx < len(data):
        A, B = map(int, data[idx].split())

        if (A, B) == (-1, -1):
            break

        population = []
        for _ in range(A):
            idx += 1
            population.append(int(data[idx]))
        
        idx += 2  # 테스트케이스 사이에 주어지는 공백 무시하고 건너뛰기

        print(binary_search(population, B))


def binary_search(population: list[int], B) -> int:
    # 각 도시의 인구 수를 mid명으로 나눴을때의 투표함 갯수 => 필요한 투표함 갯수
    # 갯수 합을 최소로 만들어야 함.
    start, end = 1, max(population)  # 맥시멈은 가장 인구가 많은 도시.
    ret = B

    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for p in population:
            cnt += (p + (mid-1)) // mid

        if cnt > B:
            start = mid + 1
        else:
            end = mid - 1
            ret = mid
    return ret


main()