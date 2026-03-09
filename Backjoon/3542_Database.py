# 자료 구조
# 문자열
# 집합과 맵
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3542
# 메모리: 97952KB / 시간: 252ms
from sys import stdin


input = stdin.readline

def main():
    n, m = map(int, input().split())

    data = [input().rstrip().split(",") for _ in range(n)]

    def check(data: list[list]) -> str:
        # db[(c1, c2, i, j)] = i, j번째 열의 값이 c1, c2인 행
        # 🚨 c1, c2값은 같으나 열 번호가 다른 경우도 있을 수 있으므로, 열 번호도 키값에 추가해줘야 함.
        # ex)
        # r1의 (i, j)열 값 = (A, B)
        # r2의 (k, l)열 값 = (A, B)
        # 위와 같은 경우, r1의 (i, j)와는 일치하지 않아도 r2의 (k, l)와는 일치하는 경우가 생길 수 있음.
        db = {}

        for r in range(n):
            for i in range(m):
                for j in range(i+1, m):
                    pair = (data[r][i], data[r][j], i, j)
                    if pair in db:
                        print("NO")
                        print(f"{db[pair] + 1} {r + 1}")
                        print(f"{i+1} {j+1}")
                        return
                    
                    db[pair] = r
        
        print("YES")
        return
    

    check(data)


main()