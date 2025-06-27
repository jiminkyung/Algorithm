# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1543

# 그냥 그리디로 풀어도 되는 문제 ㄱ-
# 왼쪽부터 target길이만큼 탐색 후 넘어가면 됨... DFS로 복잡하게 풀 필요 없다.
# ⭐DFS가 필요한 경우 -> LCS, 문자열 폭발 등등...

# 1) 그리디 풀이
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    word = input().rstrip()
    target = input().rstrip()
    target_length = len(target)

    cnt = idx = 0

    while idx <= len(word) - target_length:
        if word[idx:idx+target_length] == target:
            cnt += 1
            idx += target_length
        else:
            idx += 1
    
    print(cnt)


main()



# 2) DFS + 메모이제이션 풀이
# 메모리: 32888KB / 시간: 3936ms
import sys


sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def main():
    word = input().rstrip()
    L = len(word)
    target = input().rstrip()

    # memo[a]: a번째 인덱스부터 탐색했을때의 최대 등장 횟수
    memo = {}

    def dfs(idx, cnt, target):
        nonlocal memo

        if idx == L:
            return cnt

        if idx in memo:
            return memo[idx]

        max_cnt = 0

        for i in range(idx, L):
            if i + len(target) <= L and word[i : i + len(target)] == target:
                max_cnt = max(max_cnt, dfs(i + len(target), cnt + 1, target))
            max_cnt = max(max_cnt, dfs(i + 1, cnt, target))

        memo[idx] = max_cnt
        return max_cnt

    print(dfs(0, 0, target))


main()