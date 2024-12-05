# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/10825
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

# 메모리: 52772KB / 시간: 324ms
from sys import stdin


input = stdin.readline

N = int(input())
students = []

for _ in range(N):
    name, kor, eng, math = input().rstrip().split()
    students.append((-int(kor), int(eng), -int(math), name))

students.sort()
for student in students:
    print(student[3])

# students 정렬 + 출력을 한번에 처리하는 법
print("\n".join(map(lambda x: x[3], students)))