# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1041
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    """
    서로 반대되는 면은 다음과 같다.
    : 1-6, 2-5, 3-4 (0-5, 1-4, 2-3)

    최대한 최솟값을 만들기 위해 세 파츠를 고려해야함.
    - 귀퉁이용: 3면 합이 가장 작은 경우
    - 모서리용: 2면 합이 가장 작은 경우
    - 한면용: 모든 면 중 가장 작은 값

    귀퉁이 파츠는 윗면-옆면 사이에만 필요하므로 4개,
    모서리 파츠는 세로(N-1) * 4번, 가로(N-2) * 4번이 필요함.
    한면용은 윗면의 경우 ▣ 형태이므로 (N-2)*(N-2)개, 옆면용 (N-2)*(N-1)개가 필요하다.

    🚨 단, N이 1일경우 주사위 하나만 필요하므로 주사위의 합에서 최댓값만 빼주면 됨.
    """
    N = int(input())
    dice = list(map(int, input().split()))

    # 1개만 필요한경우
    if N == 1:
        print(sum(dice) - max(dice))
        return
    
    # 3면, 2면, 1면을 선택했을때의 최솟값 구하기
    three = two = 150  # 한 면의 최댓값은 50이므로 150으로 초기화
    one = min(dice)
    ret = 0

    # ⭐ 3면의 경우 ㄴ 형태로 구성되어야하므로, 선택한 면들이 서로 반대에 위치해있는지 체크해줘야함.
    for i in range(6):
        for j in range(i+1, 6):
            if j == 5-i:  # j가 i의 반댓면일경우
                continue
            two = min(two, dice[i] + dice[j])

            for k in range(j+1, 6):
                if k == 5-j or k == 5-i:  # k가 i의 반댓면이거나 j의 반댓면일경우
                    continue
                three = min(three, dice[i] + dice[j] + dice[k])
    
    # 귀퉁이용 (3면)
    ret += three * 4

    # 모서리용 (2면)
    # (N-1) * 4개에다가 (N-2) * 4개
    # two * (N-1)*4 + two * (N-2)*4
    ret += two * 4 * (2*N - 3)

    # 한면용
    # (N-2) * (N-1) * 4개에다가 (N-2) * (N-2)
    # one * (N-2) * (N-1) * 4 + one * (N-2) * (N-2)
    ret += one * (N-2) * (5*N - 6)

    print(ret)


main()