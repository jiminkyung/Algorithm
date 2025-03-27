# 그리디 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/1092
# 풀긴 풀었으나 훨씬 간단한 풀이가 존재함. 다시 풀어봐야할 문제.

# 1) 내 풀이. 단순무식한 풀이!
# 실제 작업을 생각하며 풀었음... 크레인의 사용상황을 매번 체크함.
# 메모리: 33432KB / 시간: 3728ms
from sys import stdin


input = stdin.readline

def main():
    # 1. 크레인과 박스 모두 내림차순으로 정렬
    N = int(input())
    crane = sorted(map(int, input().split()), reverse=True)
    M = int(input())
    boxes = sorted(map(int, input().split()), reverse=True)

    used = [False] * M  # 해당 박스 처리 유무를 나타냄
    time = 0

    # 2. 0번째 박스부터 차례대로 체크
    for i in range(M):
        # 이미 처리한 박스라면 패스
        if used[i]:
            continue
        box = i  # box: 박스 인덱스
        crn = 0  # crn: 크레인 인덱스
        while box < M and crn < N:
            # 이미 처리한 박스거나 크레인 허용무게보다 무거운 박스라면, 박스 인덱스를 1 증가시킨 뒤 넘어감
            if used[box] or crane[crn] < boxes[box]:
                box += 1
                continue
            used[box] = True
            box += 1
            crn += 1
        time += 1
    
    # 3. 모든 박스를 처리하지 못했다면 -1 출력
    print(time if all(used) else -1)


main()


# 2) 훨씬 효율적인 풀이. 크레인과 박스를 한번씩만 순회함.
# 출처👉 https://www.acmicpc.net/source/84360154

import sys
input = sys.stdin.readline

# 마찬가지로 내림차순 정렬
n = int(input())
c = sorted(list(map(int, input().split())), reverse = True)
m = int(input())
b = sorted(list(map(int, input().split())), reverse = True)

# 가장 무거운 박스가 가장 큰 무게 제한보다 무거우면 불가능
if b[0] > c[0]:
    print(-1)
    sys.exit()

M = 0  # 필요한 최소 시간
idx = 0  # 현재까지 처리된 박스의 인덱스

# 크레인을 무게 제한이 큰 순서대로 순회
for i in range(n):
    if idx == m:  # 모든 박스가 처리되었으면 종료
        break
    
    # 마지막 크레인인 경우, 남은 모든 박스 처리
    if i + 1 == n:
        while idx < m:
            idx += 1
    # 마지막 크레인이 아닌 경우
    else:
        # 현재 크레인과 다음 크레인 사이의 무게 경계에 있는 박스들 찾기
        # 즉, 다음 크레인으로는 처리할 수 없는 박스들의 수를 계산
        while idx < m and b[idx] > c[i+1]:
            idx += 1
    
    # 필요한 최소 시간 계산 및 업데이트
    # (idx+i)//(i+1)는 올림 나눗셈을 구현한 수식: ceil(idx / (i+1)) = (idx + (i+1) - 1) // (i+1) = (idx + i) // (i+1)
    # - idx: 현재 무게 범위의 박스 개수
    # - i+1: 이 무게 범위의 박스를 처리할 수 있는 크레인 개수
    # - 이 무게 범위가 병목이 될 수 있는 최소 시간 계산
    M = max(M, (idx+i) // (i+1))

print(M)