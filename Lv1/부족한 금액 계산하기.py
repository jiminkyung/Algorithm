def solution(price, money, count):
    cost = sum(i for i in range(price, price*count+1, price))
    ret = money - cost
    return -(ret) if ret < 0 else 0

# 파이써닉한 코드.
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)