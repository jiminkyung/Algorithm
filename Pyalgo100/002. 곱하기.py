# https://100.pyalgo.co.kr/?page=2#

def solution(data):
    result = 1
    for i in data:
        result *= i
    return result if len(data) != 0 else 0

# Pyalgo100에서는 통과되지 않는 코드. 또한 eval()은 실무에서는 지양되는 함수다.
def solution(data):
    return eval("*".join([str(i) for i in data]))