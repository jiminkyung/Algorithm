# 구현
# 자료 구조
# 문자열
# 시뮬레이션
# 집합과 맵
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3022
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    student = {}
    cnt = 0

    for _ in range(N):
        name = input().rstrip()

        other = sum(student[s] for s in student if s != name)
        # 해당 학생을 카운트 하기 전, 이미 다른 학생보다 카운트 수가 높다면 체크
        if student.get(name, 0) > other:
            cnt += 1
        
        student[name] = student.get(name, 0) + 1
    
    print(cnt)


main()