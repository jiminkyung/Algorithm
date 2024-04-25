def solution(n):
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            arr.append(n)
        else:
            n = 3 * n + 1
            arr.append(n)
    return arr
# 처음에 while n == 1: 이라고 적어서 돌아가지 않았다...ㅎㅎ