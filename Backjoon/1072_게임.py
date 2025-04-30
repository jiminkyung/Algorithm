# 이분 탐색


# 문제: https://www.acmicpc.net/problem/1072
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    """
    추가할 게임 수를 이분탐색으로 구한다. 처음 범위는 1 ~ 1,000,000,000으로 설정.
    🚨 승률 계산 시 부동소수점 오류 주의!
    => (이긴게임 * 100) // 전체게임 으로 계산해줘야 함
    """
    X, Y = map(int, input().split())
    
    def binary_search(left, right, val):
        """ 추가로 진행할 게임 수 구하기 """
        while left <= right:
            mid = (left + right) // 2
            mid_val = ((Y+mid) * 100 // (X+mid))

            if mid_val <= val:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    # 기존 승률
    val = (Y * 100) // X

    # 승률이 99~100이라면 몇 판을 더 해도 승률이 변하지않으므로 -1 출력
    if val >= 99:
        print(-1)
    else:
        print(binary_search(1, 1000000000, val))


main()