def solution(n):
    battery = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            battery += 1
    return battery

# 짝수인경우 순간이동, 홀수인경우 1칸 점프