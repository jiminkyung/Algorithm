# 구현
# 자료 구조
# 집합과 맵
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3957

# 까먹을까봐 푼 문제인데... 출력 형식의 덫에 걸려버림.
# 마지막에 print(*ret)을 실행할때, ret이 존재하지 않을 경우 그냥 print()한것과 동일함. ret이 존재하는지 미리 체크후, 존재하는 경우에만 print()를 사용해야함...

# 메모리: 33432KB / 시간: 40ms
from sys import stdin


def main():
    # 재료 데이터는 공백으로 구분되어 주어짐.
    # 즉, readline으로 읽어들이면 2줄 이상일경우 잘려버림.
    data = iter(stdin.read().split())

    T = int(next(data))

    for _ in range(T):
        solve(data)
        print()


def solve(data):
    N = int(next(data))
    # dic[재료이름]: {피자1, 피자2...}
    for_ing = {}
    org_ing = {}

    for pizza in range(N):
        P = next(data)

        f_cnt = int(next(data))
        foreign = [next(data) for _ in range(f_cnt)]

        o_cnt = int(next(data))
        origin = [next(data) for _ in range(o_cnt)]

        for f in foreign:
            for_ing.setdefault(f, set()).add(pizza)
        
        for o in origin:
            org_ing.setdefault(o, set()).add(pizza)
            
    # 정확하게 같은 피자에 투입된 경우에만 쌍으로 인정
    ret = [(f_key, o_key) for f_key, f_val in for_ing.items() for o_key, o_val in org_ing.items() if f_val == o_val]
    ret.sort()  # 🚨 완전한 문자열 형태"(a, b)"로 변환하기 전 튜플 상태에서 정렬해야함.

    ret = [f"({f_key}, {o_key})" for f_key, o_key in ret]

    # 🚨 조건을 만족시키는 ret이 존재할경우에만 print 실행.
    # -> 안그러면 개행문자만 달랑 출력되어버림.
    if ret:
        print(*ret, sep="\n")


main()