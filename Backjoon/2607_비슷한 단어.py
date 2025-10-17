# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/2607

# 도움이 됐던 반례!👉 https://www.acmicpc.net/board/view/68497
# 나중에 다시 풀어볼만한 문제
# 메모리: 34908KB / 시간: 52ms
from sys import stdin
from collections import Counter


input = stdin.readline

def main():
    N = int(input())
    base = input().rstrip()
    base_cnt = Counter(base)

    ret = 0

    for _ in range(N-1):
        word = input().rstrip()
        word_cnt = Counter(word)

        # 두 단어의 길이 차
        diff = abs(len(base) - len(word))

        # 서로에게 없는 문자 or 갯수가 다른 문자라면 카운트
        # diff += 두 문자의 갯수 차이
        for key in set(base) | set(word):
            diff += abs(base_cnt[key] - word_cnt[key])
        
        # 만약 2개 이하라면 결과값에 카운트
        # 1. 두 단어가 완벽히 일치할경우 -> diff = 0
        # 2. 갯수 하나만 차이날경우 -> 길이 diff 1 + 차이 diff 1 -> diff = 2
        # 3. 길이는 같으나 문자 하나가 다를 경우 -> 길이 diff 0 + 차이 diff 2 -> diff = 2
        if diff <= 2:
            ret += 1
    
    print(ret)


main()