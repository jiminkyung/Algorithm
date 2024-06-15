# 정렬
# 메모리: 35732KB / 시간: 84ms

import sys


input = sys.stdin.readline

N = int(input())
words = list(set(input().strip() for _ in range(N)))

words.sort(key=lambda x: (len(x), x))
print(*words, sep="\n")