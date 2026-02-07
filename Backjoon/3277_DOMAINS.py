# 자료 구조
# 문자열
# 집합과 맵
# 파싱
# 트리를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3277
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # domains[도메인]: 등장횟수
    domains = {}
    
    for _ in range(N):
        dom = solve()
        domains[dom] = domains.get(dom, 0) + 1
    
    max_cnt = max(domains.values())
    ret = [key for key, val in domains.items() if val == max_cnt]

    print(max_cnt)
    print(*ret)


def solve():
    data = input().rstrip()
    
    data = data.replace("http://", "")
    # / 를 기준으로 왼쪽값, .을 기준으로 오른쪽값 추출
    data = data.split("/")[0]
    dom = data.split(".")[-1]

    return dom


main()