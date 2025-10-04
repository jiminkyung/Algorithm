# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2503

# 브루트포스 문제
# 메모리: 32412KB / 시간: 36ms
from sys import stdin
from itertools import permutations


input = stdin.readline

def main():
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    ret = 0

    # perm: 정답 후보
    for perm in permutations("123456789", 3):
        # perm과 num을 비교한 값이 s, b와 일치하는지 확인
        for num, s, b in lst:
            s_cnt = sum(a == b for a, b in zip(perm, str(num)))
            b_cnt = sum((b in perm) for b in str(num))
            b_cnt -= s_cnt  # 볼 갯수에 스트라이크도 포함되어 있으므로 빼줌

            if s != s_cnt or b != b_cnt:
                break
        else:
            ret += 1
    
    print(ret)


main()