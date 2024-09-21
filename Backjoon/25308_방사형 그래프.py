# 기하 2


# 문제: https://www.acmicpc.net/problem/25308

# 참조👉 https://toolofv.tistory.com/52?category=1228027 / https://cmj092222.tistory.com/555
# 메모리: 31120KB / 시간: 296ms
from itertools import permutations
import sys


input = sys.stdin.readline

# 점은 항상 8개이며, 각 점은 45도씩 떨어져있다.
def ccw(a, b, c):
    x1, y1 = 0, a
    x2, y2 = ((b**2)/2) ** 0.5, ((b**2)/2) ** 0.5
    x3, y3 = c, 0
    # 행렬식(신발끈 공식)을 이용하거나, 벡터의 외적을 이용하면 된다.
    # 결과값이 0보다 작거나 같으면(= 일직선이거나 시계방향이면) True를 반환.
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3) <= 0

def is_True(perm):
    return all(ccw(perm[i], perm[(i+1) % 8], perm[(i+2) % 8]) for i in range(8))

arr = list(map(int, input().split()))
perms = permutations(arr)

ret = 0
for perm in perms:
    if is_True(perm):
        ret += 1

print(ret)