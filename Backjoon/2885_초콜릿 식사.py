# 수학
# 그리디 알고리즘
# 정수론
# 비트마스킹


# 문제: https://www.acmicpc.net/problem/2885

# 비트마스킹 문제. 다른 방식으로 풀 수도 있는듯?
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    K = int(input())
    # 초콜릿 크기는 2의 제곱. 항상 반으로 나누므로 초콜릿 조각의 크기 역시 2의 제곱형태다.
    # 따라서 조각을 모아 딱 K개가 되게끔 만드려면, K를 이진수로 변환했을때의 비트값을 모두 포함하면 된다.
    target = list(bin(K)[2:])

    # 이미 2의 제곱형태라면 쪼갤 필요 X
    if 2 ** (len(target)-1) == K:
        print(K, 0)
        return

    cnt = 0
    
    # 1인 비트 중 제일 작은 자릿수를 찾아야 함.
    # 만약 K = 9라면 이진수로는 1001임. 마지막 크기 1의 조각을 얻기 위해선 2, 4 크기의 초콜릿 조각이 존재해야함.
    # 쪼갠 조각을 이진수로 표현하면 1111이므로, 적어도 4번은 쪼개야 크기 1의 조각을 얻을 수 있음.
    for i in range(len(target)-1, -1, -1):
        if target[i] == "1":
            cnt = i + 1
            break
    
    # 초기 초콜릿 사이즈는 무조건 그 다음 2의 제곱수가 되어야 함.
    # K = 9일때 얻어야 하는 초콜릿 조각은 1001, 얻게 되는 초콜릿 조각은 1111 이므로 10000 크기의 초콜릿이 필요함.
    size = 2 ** len(target)
    print(size, cnt)


main()