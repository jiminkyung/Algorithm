# 구현


# 문제: https://www.acmicpc.net/problem/1384
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    group = 0  # 그룹 번호

    while True:
        group += 1
        n = int(input())

        if n == 0:
            break

        if group > 1:  # 그룹 사이마다 공백 출력
            print()

        students = {}  # students[x]: x학생에게 폭언을 남긴 학생의 번호
        names = []     # namse: 학생들의 번호
        flag = False   # 모두 착한 학생들일경우 flag = False

        for i in range(n):
            data = input().rstrip().split()
            name, *paper = data
            students[name] = [(i-j) % n for j in range(1, n) if paper[j-1] == "N"]
            if students[name]:
                flag = True
        
        print(f"Group {group}")

        if not flag:
            print("Nobody was nasty")
            continue

        names = list(students.keys())

        for name in names:
            for num in students[name]:
                print(f"{names[num]} was nasty about {name}")


main()