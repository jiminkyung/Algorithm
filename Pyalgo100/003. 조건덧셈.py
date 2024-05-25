# https://100.pyalgo.co.kr/?page=3#

def solution(data):
    return sum(i for i in data if i % 3 != 0 and i % 5 != 0)