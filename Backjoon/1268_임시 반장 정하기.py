# 구현


# 문제: https://www.acmicpc.net/problem/1268
# 메모리: 32412KB / 시간: 308ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    data = [tuple(map(int, input().split())) for _ in range(N)]

    # friends[x]: x와 같은반이었던 학생들
    friends = [set() for _ in range(N)]

    # 각 학년마다 누가 몇반이었는지 저장
    for year in range(5):
        cls_dict = {}  # cls_dict[x]: year학년때 x반이었던 학생들
        for student in range(N):
            cls = data[student][year]
            if cls not in cls_dict:
                cls_dict[cls] = []
            cls_dict[cls].append(student)
        
        # 같은 반이었던 학생들의 친구 리스트 갱신
        for group in cls_dict.values():
            l = len(group)
            for s1 in range(l):
                for s2 in range(s1+1, l):
                    friends[group[s1]].add(group[s2])
                    friends[group[s2]].add(group[s1])
    
    max_cnt = ret = 0

    for i in range(N):
        cnt = len(friends[i])
        if max_cnt < cnt:
            max_cnt = cnt
            ret = i
    
    print(ret + 1)


main()


# 다른 풀이. 2차원 리스트 안에 set()을 추가해서 lst[학년][반] 형태로 저장함.
# 출처👉 https://www.acmicpc.net/source/79363870
# 이게 더 깔끔해보인다. 실행시간도 빠름.
import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    classes = [[set() for _ in range(10)] for _ in range(5)]
    students = [tuple(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(5):
            classes[j][students[i][j]].add(i)
    res = max_cnt = -1
    for i in range(N):
        friends = set()
        for j in range(5):
            friends |= classes[j][students[i][j]]
        cnt = len(friends)
        if cnt > max_cnt:
            max_cnt = cnt
            res = i+1
    print(res)

solution()