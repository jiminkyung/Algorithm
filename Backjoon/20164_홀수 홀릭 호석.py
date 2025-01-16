# 구현  # 브루트포스  # 재귀


# 문제: https://www.acmicpc.net/problem/20164
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = input().rstrip()

min_odd = float("inf")
max_odd = 0

# 숫자의 홀수 갯수를 계산하는 함수
def checking(num):
    cnt = 0

    for n in num:
        if int(n) % 2 != 0:
            cnt += 1
    return cnt


# 숫자를 조건에 맞게 나누어 경우의 수를 구하는 함수
def making(num, odd):
    global min_odd, max_odd

    # num의 홀수 갯수 체크
    odd += checking(num)

    # 1. 길이가 1일때 -> 최댓값, 최솟값 업데이트
    if len(num) == 1:
        min_odd = min(odd, min_odd)
        max_odd = max(odd, max_odd)
        return
    
    # 2. 길이가 2일때
    if len(num) == 2:
        new_num = str(int(num[0]) + int(num[1]))
        making(new_num, odd)
        return
    
    # 3. 길이가 3이상일때
    # 자르는 위치. i: 첫번째 위치, j: 두번째 위치
    for i in range(1, len(num)-1):  # 두번째 구간으로 올 수 있는 범위
        for j in range(i+1, len(num)):
            num1 = int(num[:i])
            num2 = int(num[i:j])
            num3 = int(num[j:])
            
            new_num = str(num1 + num2 + num3)
            making(new_num, odd)


making(N, 0)

print(min_odd, max_odd)