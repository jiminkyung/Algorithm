# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1003
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def fibonacci():
    arr = [0] * 41
    arr[1] = arr[2] = 1
    
    for i in range(3, 41):
        arr[i] = arr[i-1] + arr[i-2]
    return arr

arr = fibonacci()

for _ in range(int(input())):
    N = int(input())

    if N == 0:
        print("1 0")
    else:
        print(arr[N-1], arr[N])