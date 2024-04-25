# 짜증나서 AI선생님께 여쭤봤다.
def solution(date1, date2):
    # 연도 비교
    if date1[0] < date2[0]:
        return 1
    elif date1[0] > date2[0]:
        return 0

    # 월 비교
    if date1[1] < date2[1]:
        return 1
    elif date1[1] > date2[1]:
        return 0

    # 일 비교
    if date1[2] < date2[2]:
        return 1
    else:
        return 0

# 미친 풀이.
def solution(date1, date2):
    return int(date1 < date2)

# 이렇게 했었는데 난 왜 안됐지? 싶었던 풀이
def solution(date1, date2):
    for i in range(3):
        if date1[i]<date2[i]:return 1
        elif date2[i]<date1[i]: return 0
    return 0