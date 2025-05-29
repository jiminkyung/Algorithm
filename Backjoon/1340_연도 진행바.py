# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/1340
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    # 1월부터 차례대로 맵핑.
    # month["January"] = 0, days[0] = 31
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])}
    m, d, y, time = input().rstrip().split()

    # 윤년 체크
    y = int(y)
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        days[1] = 29

    # 1day = 24hours = 1440minutes
    total = 0  # 1년을 분으로 환산
    for i in range(12):
        total += days[i] * 1440
    
    # 입력받은 값(월, 일, 시, 분)을 분으로 환산
    passed = 0
    m = month[m]
    
    for i in range(m):
        passed += days[i] * 1440
    
    d = int(d[:-1])
    passed += 1440 * (d-1)

    hh, mm = map(int, time.split(":"))

    passed += 60 * hh
    passed += mm

    print(passed / total * 100)


main()