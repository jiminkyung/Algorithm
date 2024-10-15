# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1946

# 시간초과 코드. 2중 for문 사용시 PyPy3도 힘들다...🥲
from sys import stdin


input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    
    for a, b in score:
        for c, d in score:
            if a == c:
                continue
            if a > c and b > d:
                cnt += 1
                break
    print(N - cnt)


# 참고👉 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1946-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90-%EC%8B%A4%EB%B2%841-%EA%B7%B8%EB%A6%AC%EB%94%94
# 메모리: 58552KB / 시간: 3224ms
"""
입력데이터는 (서류 등수, 면접 등수) 로 주어진다.
만약 어떤 사람의 점수가 (2, 5)일때, 다른 사람들 중 (1, 4)가 있다면 탈락된다.
1. 서류등수 순으로 정렬.
2. 1등의 면접등수를 top으로 저장.
3. 서류등수 1등은 무조건 통과이므로, 2등부터 N등까지 체크한다.
=> 만약, 현재 사람의 면접등수가 top보다 높다면 합격인 셈이다.
=> 위 조건에 부합하면 top을 현재 사람의 면접등수로 변경.
부합하지 않는다면, 현재 사람보다 서류등수, 면접등수 모두 높은 경우가 있다는 뜻이므로 탈락된다.
"""
from sys import stdin


input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [tuple(map(int, input().split())) for _ in range(N)]
    score.sort()
    cnt = 1
    
    top = score[0][1]

    for i in range(1, N):
        if score[i][1] < top:
            top = score[i][1]
            cnt += 1
    
    print(cnt)