# 정렬
# 문자열


# 문제: https://www.acmicpc.net/problem/1622
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


def main():
    data = stdin.read().splitlines()

    for i in range(0, len(data), 2):
        a, b = data[i], data[i+1]

        # 공통되는 문자열 추출
        same = set(a) & set(b)
        ret = ""

        for s in same:
            # 공통되는 횟수만큼 ret에 추가
            cnt = min(a.count(s), b.count(s))
            ret += s * cnt
        
        print("".join(sorted(ret)))


main()