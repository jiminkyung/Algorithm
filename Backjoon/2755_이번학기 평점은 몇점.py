# 문제: https://www.acmicpc.net/problem/2755


# 파이썬은 오사오입(banker's rounding)을 사용한다.
# ret = 3.275일때 print(round(ret, 2))를 실행하면 3.27로 반환됨.
# 하지만 아래처럼 327.5로 만들어준 뒤 round()를 사용하면 328이 반환된다.

# 부동소수점 오차 때문인가? 반올림하고자 하는 자리에 해당하는 값에 따라 0.1, 0.01등을 더해준 뒤 round()를 사용해야될듯.

# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline
grade = {"A+": 4.3, "A0": 4.0, "A-": 3.7,
        "B+": 3.3, "B0": 3.0, "B-": 2.7,
        "C+": 2.3, "C0": 2.0, "C-": 1.7,
        "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
total_credit = ret = 0

for _ in range(int(input())):
    _, credit, score = input().rstrip().split()
    total_credit += int(credit)
    ret += grade[score] * int(credit)

ret /= total_credit
r = round(ret * 100) / 100
print(f"{r:.2f}")