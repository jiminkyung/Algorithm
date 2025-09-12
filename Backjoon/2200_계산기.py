# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/2200
# 메모리: 33432KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    """
    잘 보면 x는 최고 차수만큼만 곱해진다.
    x^3 + 12x^2 + 4x = x, +, 1, 2, *, x, + 4, *, x
    
    따라서 전체 x 갯수는 N개, x 앞에 위치하는 연산자는 N-1개가 된다.
    -> 초기 cnt값을 N*2 - 1로 설정.

    그 다음, 최고차항을 제외한 계수들을 하나씩 체크한다.
    (최고차항의 계수는 항상 1이므로 더 연산할 필요 X)
    숫자는 한 자리씩 입력해야하므로 len(숫자)만큼 눌러야 한다.
    그리고 숫자의 앞에는 + 연산자가 들어가므로, 각 계수당 횟수는 len(숫자) + 1이 된다.

    마지막으로 = 연산자까지 포함 -> cnt + 1
    """
    N = int(input())
    degrees = input().rstrip().split()

    cnt = N * 2 - 1
    for d in degrees[1:]:
        if d == "0":
            continue

        cnt += len(d) + 1
        
    print(cnt + 1)


main()