# 수학
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1198
# 메모리: 32412KB / 시간: 56ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # "연속"된 세 점을 선택해야 함.
    # 🗝️ 하지만 i, i+1, i+2를 선택했을때 i+1번째 점이 탈락되고, 남은 점들로 j, j+1, j+2를 선택하고... 를 반복하다보면,
    # 무작위로 세 점을 선택하는 것과 같은 결과가 나오게 된다.

    def triangle(p1, p2, p3) -> float:
        """ 삼각형 넓이 구하기 (신발끈 공식) """
        shoe = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p2[0]*p1[1] - p3[0]*p2[1] - p1[0]*p3[1]
        return abs(shoe) / 2
    

    max_ret = 0

    for p1 in range(N):
        for p2 in range(N):
            for p3 in range(N):
                if p1 != p2 != p3:  # 각기 다른 세 점을 꼭짓점으로 선정
                    ret = triangle(points[p1], points[p2], points[p3])
                    max_ret = max(ret, max_ret)
    
    print(max_ret)


main()