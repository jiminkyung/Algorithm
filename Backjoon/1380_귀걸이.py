# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/1380

# 1) 처음 풀이
# 입력 데이터 조건(2n-1줄만 주어짐)을 못보고 풀이...
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    scene = 0

    while True:
        data = input().rstrip()

        if data.isdigit():
            scene += 1
            if scene > 1:
                for i in range(1, n+1):
                    if visited[i] == 0:
                        print(scene-1, students[i])
            if data == "0":
                break

            n = int(data)
            students = {i: input().rstrip() for i in range(1, n+1)}
            visited = [-1] * (n+1)
        else:
            number = int(data.split()[0])
            if visited[number] == -1:
                visited[number] = 0
            elif visited[number] == 0:
                visited[number] = 1


main()


# 2) 수정한 풀이
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # 딱 한명의 학생만 귀걸이를 찾지 못함.
    # => (학생번호, A/B)는 2n-1줄만 주어짐.
    scene = 1

    while True:
        n = int(input())

        if n == 0:
            break

        students = {i: input().rstrip() for i in range(1, n+1)}
        visited = [-1] * (n+1)

        # 학생의 번호만 체크
        for _ in range(2*n - 1):
            num = int(input().split()[0])

            # -1: 착용중, 0: 뺏김, 1: 돌려받음
            if visited[num] == -1:
                visited[num] = 0
            elif visited[num] == 0:
                visited[num] = 1
        
        # 시나리오 번호, 뺏긴 상태인 학생의 이름 출력
        for i in range(1, n+1):
            if visited[i] == 0:
                print(scene, students[i])
        
        scene += 1


main()