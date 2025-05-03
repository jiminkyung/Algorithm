# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1105
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    1. L과 R의 자릿수가 다르다면
        - 자릿수가 L보다 크고 R보다 작은 숫자 중 8이 전혀 없는 숫자를 만들 수 있음
        - ex) L=999, R=10000 이면 1000~9999 중 1111과 같이 8이 없는 수가 있음
        - 따라서 답은 0
    
    2. L과 R의 자릿수가 같다면
        - 왼쪽부터 숫자를 하나씩 비교
        - L과 R의 같은 자리에 같은 숫자가 있고, 그 숫자가 8이면 무조건 포함해야 함
        - L과 R의 같은 자리에 다른 숫자가 있으면, 이후 자리는 8을 포함하지 않아도 됨
        - ex) L=8808, R=8880이면 앞의 두 자리 "88"은 무조건 포함, 나머지는 선택 가능
    """
    L, R = input().rstrip().split()
    L_len, R_len = len(L), len(R)

    if L_len != R_len:
        print(0)
        return
    
    cnt = 0

    for i in range(L_len):
        if L[i] != R[i]:
            break
        if L[i] == "8":
            cnt += 1
    
    print(cnt)


main()