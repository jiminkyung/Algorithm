# 구현


# 문제: https://www.acmicpc.net/problem/1308
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 현재날짜 ~ 미래날짜 일수를 직접 계산하려고 했으나, 비효율적임.
    # 🗝️1년 1월 1일부터 현재/미래 날짜까지의 일수를 계산하고 빼주는게 깔끔하다.
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())

    # 1000년이 넘어가면 gg
    if y1 + 1000 < y2 or (y1 + 1000 == y2 and (m1, d1) <= (m2, d2)):
        print("gg")
        return
    
    # year[x]: x가 윤년이면 True, 아니면 False
    year = [False] * 10000

    for i in range(4, 10000, 4):
        year[i] = True
    for i in range(100, 10000, 100):
        year[i] = False
    for i in range(400, 10000, 400):
        year[i] = True
    
    def calc(y, m, d):
        """ 1년 1월 1일 ~ y년 m월 d일까지의 일수 계산 """
        days = 0

        for i in range(1, y):  # y-1, m-1까지 계산해야함.
            days += 365 + int(year[i])
        for i in range(1, m):
            days += month[i] + int(year[y] and i == 2)
        
        days += d
        return days
    

    diff = calc(y2, m2, d2) - calc(y1, m1, d1)
    print(f"D-{diff}")


main()