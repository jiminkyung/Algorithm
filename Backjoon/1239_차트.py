# 브루트포스 알고리즘
# 순열


# 문제: https://www.acmicpc.net/problem/1239

# 반례에 막힘... 반례👉 https://www.acmicpc.net/board/view/90460
# 참고한 풀이👉 https://365waytobe-pro-grammer.tistory.com/115

# 그리고 훨씬 효율적인 풀이👉 https://www.acmicpc.net/source/85531384
# ↪️ 첫번째 원소를 고정시켜서 n!을 (n-1)!로 만들 수 있음.


# 1) 효율적인 풀이 참고
# 메모리: 32544KB / 시간: 48ms
from sys import stdin
from itertools import permutations


input = stdin.readline

def main():
    N = int(input())
    chart = list(map(int, input().split()))

    # 가장 큰 퍼센티지가 50을 넘어간다면 직선을 만들 수 없음
    if max(chart) > 50:
        print(0)
        return


    def make_sum(perm: tuple) -> int:
        """ 누적합으로 정확히 50이 되는 구간들을 카운트 """
        prefix_sum = [chart[0]]
        curr_sum = chart[0]

        for p in perm:
            curr_sum += p
            prefix_sum.append(curr_sum)
        
        # 구간 i - j == 50이라면, 직선이 하나 생성되는 형태임.
        cnt = 0
        for i in range(len(perm)):
            for j in range(i+1, len(perm)+1):
                if prefix_sum[j] - prefix_sum[i] == 50:
                    cnt += 1
        # if cnt == 2:
        #     print(f"순열은 {perm}, 합 리스트는 {prefix_sum}")
        return cnt
    
    ret = 0

    for perm in permutations(chart[1:], N-1):
        ret = max(ret, make_sum(perm))
    
    print(ret)


main()


# 2) 첫번째 풀이
# 메모리: 32544KB / 시간: 136ms
from sys import stdin
from itertools import permutations


input = stdin.readline

def main():
    N = int(input())
    chart = list(map(int, input().split()))

    if max(chart) > 50:
        print(0)
        return


    def make_sum(perm: tuple) -> int:
        """ 누적합으로 정확히 50이 되는 구간들을 카운트 """
        prefix_sum = []
        curr_sum = 0

        for p in perm:
            curr_sum += p
            prefix_sum.append(curr_sum)
        
        cnt = 0
        for i in range(len(perm)-1):
            for j in range(i+1, len(perm)):
                if prefix_sum[j] - prefix_sum[i] == 50:
                    cnt += 1
        # if cnt == 2:
        #     print(f"순열은 {perm}, 합 리스트는 {prefix_sum}")
        return cnt
    
    ret = 0

    for perm in permutations(chart):
        ret = max(ret, make_sum(perm))
    
    print(ret)


main()