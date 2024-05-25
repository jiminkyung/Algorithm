# https://100.pyalgo.co.kr/?page=7#

def solution(data):
    return [item[0] for item in sorted(data, key=lambda x: x[1])]