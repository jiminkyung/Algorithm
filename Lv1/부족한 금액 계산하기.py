def solution(price, money, count):
    cost = sum(i for i in range(price, price*count+1, price))
    ret = money - cost
    return -(ret) if ret < 0 else 0