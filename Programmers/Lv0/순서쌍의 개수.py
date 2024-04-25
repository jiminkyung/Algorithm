def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt

# 다른분이 작성한 한줄 코드...인데 별로 좋아보이진 않는다.
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))