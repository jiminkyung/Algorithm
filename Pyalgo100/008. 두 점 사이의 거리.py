# https://100.pyalgo.co.kr/?page=8#

def solution(data):
    x = list(zip(data, data[1:])) # [1, 3], [3, 4]...
    return list(sorted(x, key = lambda x: abs(x[1] - x[0]))[0]) # list로 또 묶어줘야하나? -> 묶어줘야함.

# zip(data, data[1:])은 써먹기 좋은 방법이다. 비슷한 문제가 나오면 떠올리도록.