# 문자열


# 문제: https://www.acmicpc.net/problem/2908
# 메모리: 31120KB / 시간: 32ms
A, B = input().split()
print(max(int(A[::-1]), int(B[::-1])))