# https://100.pyalgo.co.kr/?page=4#

def solution(data):
    cookies = [i.split()[1][:-1] for i in data] # 갯수만 뽑아냄.
    result = 0
    for order, cookie in enumerate(cookies, 1):
        result += order * int(cookie) # str형이므로 변환해줌.
    return result