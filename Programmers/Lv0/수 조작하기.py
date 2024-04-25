def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n

# zip을 사용한 간결한 풀이! 머리를 쓰고 살자 ㅎㅎㅎㅎ
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

# count를 사용하는 방법도 있다. 그래도 위 코드가 더 이쁜듯.
def solution(n, control):
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))