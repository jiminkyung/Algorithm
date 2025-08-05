# 수학
# 정수론


# 문제: https://www.acmicpc.net/problem/1862

# 진법 변환 문제
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = list(map(int, input().rstrip()))
    L = len(N)
    ret = 0

    # 각 자릿수를 체크한다.
    # 🗝️4 이상이면 -1, 미만이면 그대로.
    # 🗝️변환시킨 수는 9진법인 셈. 이걸 다시 10진법으로 계산한다.
    # ex) 15 -> [1, 4] -> 1 x 9^1 + 4 x 9^0 => 13
    for i, num in enumerate(N, start=1):
        if num >= 4:
            num -= 1
        
        ret += num * (9 ** (L-i))
    
    print(ret)


main()