def solution(num):
    ret = 0
    
    while ret < 500:
        if num == 1:
            return ret

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        ret += 1

    return -1