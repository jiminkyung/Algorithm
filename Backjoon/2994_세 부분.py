# 구현
# 문자열
# 브루트포스 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/2993
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    word = input().rstrip()
    L = len(word)
    comb = []

    # 첫번째 지점 (처음 ~ i까지)
    for i in range(L-2):
        c1 = word[i::-1]
        # 두번째 지점 (i+1 ~ j까지)
        for j in range(i+1, L-1):
            c2 = word[j:i:-1]
            c3 = word[:j:-1]  # 나머지 (j+1 ~ 끝까지)

            comb.append(c1 + c2 + c3)
    
    # 정렬 후 제일 첫번째 단어 출력
    comb.sort()
    print(comb[0])


main()