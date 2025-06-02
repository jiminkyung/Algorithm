# 조합론
# 확률론
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1359


# 모든 경우의 수를 체크하는 풀이, "같을 경우"를 가정해서 계산한 풀이 모두 실행시간은 같음.
# 데이터가 그리 크지 않아서 가능한듯?

# 1) 지민이의 수를 고정하고, 컴퓨터의 수를 계산
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M, K = map(int, input().split())

    # 지민이가 고른 M개의 수와 컴퓨터가 고른 수 중 K개 이상이 같을 경우
    ret = 0

    def combination(num: int, cnt: int) -> int:
        if cnt == 0:
            return 1
        
        top = bottom = 1

        for i in range(num, num-cnt, -1):
            top *= i

        for i in range(cnt, 0, -1):
            bottom *= i
        
        return top // bottom  # 경우의 수 반환

    
    # 지민이가 고른 M 개중 i개가 같고 M-i개가 같지 않을 경우
    for i in range(K, M+1):
        ret += combination(M, i) * combination(N-M, M-i)
    
    total = combination(N, M)
    print(ret / total)


main()


# 2) combinations 모듈로 모든 경우의 수를 직접 계산
# 메모리: 32412KB / 시간: 36ms
from sys import stdin
from itertools import combinations


input = stdin.readline

def main():
    N, M, K = map(int, input().split())

    lst = list(combinations(range(1, N+1), M))

    total = win = 0

    for jimin in lst:
        for resort in lst:
            total += 1
            same = len(set(jimin) & set(resort))

            if K <= same:
                win += 1
    
    print(win / total)


main()