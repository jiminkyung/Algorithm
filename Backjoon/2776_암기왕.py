# 자료 구조
# 정렬
# 이분 탐색
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/2776


# 이분탐색으로 분류된 문제이지만, Python3론 이분탐색 풀이 ❌
# 단순하게 set을 사용하니 통과됐다... 다른 풀이들도 찾아봤으나 모두 set 활용.

# 처음 풀이는 nums_2를 dict로 설정했었으나 틀림.
# 반례👉 https://ideone.com/c0jFX1 / 출처는 https://www.acmicpc.net/board/view/54272
# => 요약하면 nums_2에 중복이 있을수도 있음.

# 메모리: 227240KB / 시간: 1192ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    def solve():
        N = int(input())
        nums_1 = set(map(int, input().split()))
        M = int(input())
        nums_2 = list(map(int, input().split()))
        ret = [int(num in nums_1) for num in nums_2]  # 있으면 1 없으면 0

        print(*ret, sep="\n")
    

    for _ in range(T):
        solve()


main()