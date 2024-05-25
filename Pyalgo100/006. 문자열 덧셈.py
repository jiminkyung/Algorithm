# https://100.pyalgo.co.kr/?page=6#

def solution(data):
    return sum(map(int, [i for i in data if i.isdigit()])) # 숫자만 뽑아주고, int형으로 변환한 뒤 sum.