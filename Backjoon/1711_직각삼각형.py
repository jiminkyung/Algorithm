# 기하학  # 피타고라스 정리
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1711

# 1) Python3 통과 풀이 (벡터의 내적)
# 메모리: 33432KB / 시간: 3036ms
from sys import stdin


input = stdin.readline

def main():
    # 🗝️벡터의 내적을 이용하여 구하는 방법이다. Python으로 통과 가능.
    # 두 방향벡터의 내적이 0이라면 -> 서로 수직(직각)
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    total = 0
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    
    # 1. 점 i를 기준으로 삼고, i->j의 방향벡터 구하기
    for i in range(N):
        x, y = coord[i]
        direction = {}

        for j in range(N):
            if i == j:
                continue
            nx, ny = coord[j]
            dx, dy = nx - x, ny - y

            # 2. 좌표 압축
            # => 같은 방향의 점들을 하나로 묶음.
            g = gcd(abs(dx), abs(dy))
            curr_direction = (dx//g, dy//g)
            direction[curr_direction] = direction.get(curr_direction, 0) + 1
        
        # 3. 방향벡터를 하나씩 순회하며, 해당 벡터의 갯수와 수직인 벡터의 갯수를 곱한다.
        # (x, y)와 수직이려면 (-y, x) or (y, -x) 여야 함.
        # 중복 방지를 위해 (-y, x)만 체크할거임.
        # 예를들어, (2, 3), (-3, 2), (3, -2)가 있다고 가정해보자.
        # (-3, 2), (3, -2) 모두 (2, 3)과 수직이지만, 코드상으로는 (-3, 2)만 체크하는셈이다.
        # 그럼 (3, -2)는??
        # -> (dx, dy) == (3, -2)일때, (2, 3)을 체크하게 됨. 자연스럽게 모든 수직의 경우를 확인하게 된다.
        for (dx, dy), cnt in direction.items():
            op_cnt = direction.get((-dy, dx), 0)
            total += cnt * op_cnt
    
    print(total)


main()


# 2) PyPy3 통과 풀이 (브루트 포스)
# 메모리: 111420KB / 시간: 5028ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 세 변을 기준으로 체크
    for i in range(N):
        x1, y1 = coord[i]
        for j in range(i+1, N):
            x2, y2 = coord[j]
            c = (x2-x1) ** 2 + (y2-y1) ** 2
            for k in range(j+1, N):
                x3, y3 = coord[k]
                a = (x3-x2) ** 2 + (y3-y2) ** 2
                b = (x3-x1) ** 2 + (y3-y1) ** 2
                
                # (가장 긴 변)^2 = 변^2 + 변^2 을 만족하면 직각삼각형 (피타고라스)
                if a+b == c or b+c == a or a+c == b:
                    cnt += 1
    
    print(cnt)


main()