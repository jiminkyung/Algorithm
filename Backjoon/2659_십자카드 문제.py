# 구현
# 브루트포스 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/2659
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    num = "".join(input().rstrip().split())
    target = int(num)
    visited = set()

    # 🚨무조건 sort하면 안됨. "시계"방향으로 선택해야 함.
    # target의 시계수 확인
    for i in range(4):
        tmp = int(num[i:] + num[:i])
        if tmp < target:
            target = tmp
    
    cnt = 0
    for i in range(1111, 10000):  # 1111 ~ 9999
        s = str(i)

        # 1 ~ 9의 숫자만 들어있으므로 0이 포함되면 건너뜀
        if "0" in s:
            continue

        # 현재 숫자의 시계수 후보들 중, 이미 확인했던 수가 있다면 넘어감. (앞에서 나온 수가 제일 작은 시계수이므로)
        for j in range(4):
            tmp = s[j:] + s[:j]
            if tmp in visited:
                break
        else:
            visited.add(s)
            cnt += 1
        
        # 현재 숫자가 target 이상이라면 출력
        # -> 정확히 target일때 출력하도록 해도 됨. (i == target)
        if i >= target:
            print(cnt)
            break


main()