# 내 원래 답. 테스트케이스 1, 10 실패.
def solution(dots):
    lst = list(zip(*dots))
    l, x = lst[0], lst[1]
    l1, l2, l3, l4 = [*l]
    x1, x2, x3, x4 = [*x]

    if abs(l1 - l2) == abs(l3 - l4) and abs(x1 - x2) == abs(x3 - x4):
        return 1
    elif abs(l1 - l3) == abs(l2 - l4) and abs(x1 - x3) == abs(x2 - x4):
        return 1
    elif abs(l1 - l4) == abs(l2 - l3) and abs(x1 - x4) == abs(x2 - x3):
        return 1
    else:
        return 0

# 기울기를 비교하는것으로 변경해봄. 통과.
def solution(dots):
    lst = list(zip(*dots))
    x, y = lst[0], lst[1]
    x1, x2, x3, x4 = [*x]
    y1, y2, y3, y4 = [*y]

    if (abs(y1-y2)/abs(x1-x2)) == (abs(y3-y4)/abs(x3-x4)):
        return 1
    elif (abs(y1-y3)/abs(x1-x3)) == (abs(y2-y4)/abs(x2-x4)):
        return 1
    elif (abs(y1-y4)/abs(x1-x4)) == (abs(y2-y3)/abs(x2-x3)):
        return 1
    return 0

# 근데 안이쁘다ㅜㅜ