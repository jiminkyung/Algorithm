# 수학


# 문제: https://www.acmicpc.net/problem/1117

# 처음에 생각한 방법: 접힐때마다 해당 좌표를 새로운 좌표에 연결시켜줌
# 두번째로 생각한 방법: ㄴㄱㄴ 형식으로 위/아래가 이어짐. 데칼코마니 모양이니 왼쪽 색칠넓이 * 높이 + 오른쪽 색칠넓이 * 높이 를 구함
# 두번째 방식이 옳은것같은데, 좌표 계산 과정에서 꼬임...
# => 클로드에게 물어봤고 따라해봤지만 틀렸다 ㅋ 아래는 틀린 코드를 참고해서 수정한 코드.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # f: 세로로 접는 좌표, c: 접는 횟수 (실질적으로 만들어지는 칸은 c+1개)
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
    
    # 전체 종이 면적
    total = W * H

    # 색칠된 직사각형의 세로 길이
    height = y2 - y1
    colored = 0

    # f = W 이라면 접은 후의 면적 = 왼쪽 면적이기 때문에 패스.
    if f < W:
        # 접은 후 오른쪽 종이에서의 x1, x2
        # 오른쪽 면적의 범위는 f ~ W 이어야 함.
        right_x1 = min(W, x1 + f)
        right_x2 = min(W, x2 + f)

        if right_x1 < right_x2:
            right_width = right_x2 - right_x1
            colored += right_width * height
    
    # 마찬가지로 f = 0 이라면 접은 후의 면적 = 오른쪽 면적이 되어버리므로 패스.
    if f > 0:
        """
        처음엔 2f-x2, 2f-x1을 비교값으로 넣어줬음.
        -> 예제 3 실행시 136이 나와버림. 왼쪽 부분이 범위를 벗어난다고 판단해버린것.

        x: 접기 전 좌표, nx: 접은 후 전체 기준 좌표일때,
        nx = 2f-x, x = 2f-nx가 되므로, 2f-x2는 틀린 계산법임.
        위처럼 작성해버리면 2f-x2(x1) => 8, 2f-x1(x2) => min값으로 7이 나와서 x1 < x2를 만족하지 못함.
        -> 이 식을 사용하려면, 오른쪽 종이 기준에서의 x1, x2를 사용해야함.
        -> 2f - (x2 + f), 2f - (x1 + f)

        간단히 생각해보면 데칼코마니같은 형식이니까,
        r_x1, r_x2 = x1 + f, x2 + f이므로 l_x1, l_x2 = f - x2, f - x1가 되는게 맞음.
        """
        # 접은 후 왼쪽에서의 x1, x2
        # 왼쪽 면적의 범위는 0 ~ f
        left_x1 = max(0, f - x2)
        left_x2 = max(0, f - x1)

        if left_x1 < left_x2:
            left_width = left_x2 - left_x1
            colored += left_width * height
    
    # c+1개만큼 곱해주기
    colored *= (c+1)
    
    print(total - colored)


main()