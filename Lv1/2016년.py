def solution(a, b):
    # 2월은 1월(31일)이 지난 후, 3월은 2월(29일)이 지난 후... 이런식으로.
    month = {1: 0, 2: 31, 3: 29, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30}
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    date = sum(month[i] for i in range(2, a+1)) + b
    return day[date % 7 - 1]