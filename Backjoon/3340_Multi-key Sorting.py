# 자료 구조
# 정렬
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/3340
# 메모리: 99588KB / 시간: 224ms
from sys import stdin


input = stdin.readline

def main():
    # 최종적으로 실행된 정렬만 확인해보면 됨.
    # 1 2 1 2 3 3 -> 앞에 실행된 1 2 는 의미 없음. 뒤에 1 2 가 중요.
    # 또한 3 3 3 처럼 중복된것도 한번만 체크하면 됨.
    C, N = map(int, input().split())
    lst = list(map(int, input().split()))

    ret = []
    used = set()

    # 뒤에서부터 중복 없이 체크.
    for i in range(N-1, -1, -1):
        if lst[i] not in used:  # 이미 확인한 정렬이라면 패스
            ret.append(lst[i])
            used.add(lst[i])
    
    print(len(ret))
    print(*ret[::-1])


main()