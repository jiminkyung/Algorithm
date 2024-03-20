def solution(n):
    ret = 0
    for i in range(2, n+1):
        is_prime = True
        x = int(i**0.5)
        for k in range(2, x+1):
            if i % k == 0:
                is_prime = False
                break
        if is_prime:
            ret += 1
    return ret

# 다른분의 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)