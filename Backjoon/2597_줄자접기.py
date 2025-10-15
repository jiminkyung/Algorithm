# 구현


# 문제: https://www.acmicpc.net/problem/2597

# 여러가지 테스트 케이스를 돌려보는게 좋음. 구현 연습 시 다시 풀어볼만한 문제.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    L = int(input())
    red = list(map(float, input().split()))
    blue = list(map(float, input().split()))
    yellow = list(map(float, input().split()))

    r1, r2 = red
    b1, b2 = blue
    y1, y2 = yellow

    def new_point(p: float, mid: float, dir: str):
        # 1. 왼쪽 < 오른쪽일경우. 왼쪽을 오른쪽 위로 접음.
        if dir == "left":
            # 🚨왼쪽이 오른쪽 위로 접히는 경우 전체적으로 길이 갱신을 해줘야 함.
            # 안그러면 실질적인 길이보다 긴 값(좌표 기준)이 L로 저장되어버림.
            if p < mid:
                p = mid + (mid - p)
            p -= mid
        # 2. 왼쪽 >= 오른쪽일경우. 오른쪽을 왼쪽 위로 접음.
        else:
            if p > mid:
                p = mid - (p - mid)
        return p
    
    # 빨강 맞춤
    mid = (r1 + r2) / 2
    left, right = mid, L - mid
    L = max(left, right)

    dir = "left" if left < right else "right"
    b1 = new_point(b1, mid, dir)
    b2 = new_point(b2, mid, dir)
    y1 = new_point(y1, mid, dir)
    y2 = new_point(y2, mid, dir)

    # 파랑 맞춤
    if b1 != b2:
        mid = (b1 + b2) / 2
        left, right = mid, L - mid
        L = max(left, right)

        dir = "left" if left < right else "right"
        y1 = new_point(y1, mid, dir)
        y2 = new_point(y2, mid, dir)
    
    # 노랑 맞춤
    if y1 != y2:
        mid = (y1 + y2) / 2
        left, right = mid, L - mid
        L = max(left, right)
    
    print(f"{L:.1f}")  # 소수점 한자리에서 출력


main()