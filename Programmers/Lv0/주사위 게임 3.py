"""
이리저리 헤매다가 겨우 짰지만 너무 길다...^^
다른분들 코드 보니 10줄은 적은 경우도 있다.
굳이 딕셔너리를 쓰지 않고 각 정수의 카운트값을 리스트로 담아줬어도 됐는데ㅜㅜ

여튼 이리저리 생각해볼만한 문제였다.
"""

def solution(a, b, c, d):
    result = 0
    arr = [a, b, c, d]
    dic = {i:arr.count(i) for i in arr}
    sorted_dic = sorted(dic, key=lambda x: dic[x])

    if len(dic) == 1:
        result = 1111 * a
    elif len(dic) == 2:
        if max(dic.values()) == 3:
            p = sorted_dic[1]
            q = sorted_dic[0]
            result = (10 * p + q) ** 2
        else:
            p, q = sorted_dic
            result = (p + q) * abs(p - q)
    elif len(dic) == 3:
        p = sorted_dic[2]
        q, r = sorted_dic[0], sorted_dic[1]
        result = q * r
    else:
        result = min(dic)
    return result