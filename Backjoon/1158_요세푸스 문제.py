# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1158
# 메모리: 34016KB / 시간: 52ms
from sys import stdin
from collections import deque


input = stdin.readline

N, K = map(int, input().split())
circle = deque(list(map(str, range(1, N+1))))

ret = []
for _ in range(N):
    circle.rotate(-K)
    ret.append(circle.pop())

print(f"<{', '.join(ret)}>")


# deque을 사용하지 않은 풀이.
# 출처👉 https://www.acmicpc.net/source/84611841
n,k = map(int, input().split())
yo = [i+1 for i in range(n)]
answer = []
i = 0
for _ in range(n):
    i = (i+k-1)%len(yo)  # 리스트의 끝을 넘어가면 처음으로 돌아가야하기 때문에 % len(yo)를 해준다.
    answer.append(yo.pop(i))
print("<"+str(answer)[1:-1]+">")