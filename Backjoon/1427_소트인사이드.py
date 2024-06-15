# 정렬
# 메모리: 31252KB / 시간: 40ms

import sys


N = list(map(int, list(sys.stdin.readline().strip())))
N.sort(reverse=True)

print(*N, sep="")