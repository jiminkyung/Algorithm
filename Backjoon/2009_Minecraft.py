# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2009

# 결과값 M은 여러 모양으로 만들어질 수 있음.

# 1) 후보 칸을 모두 채워넣는 방식
# 참고로 M을 만든 후 조건을 만족하는지 체크하는 과정을 더 짧게 줄일수도 있다.
# 👉 https://www.acmicpc.net/source/88252967
    # arr 저장 시 H', R', C'에도 1을 저장하고 H = H'인지 체크하는 방식.

# 메모리: 40748KB / 시간: 448ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())

    def check(n: int):
        # 결과값 M을 저장할 리스트
        arr = [[[0] * n for _ in range(n)] for _ in range(n)]

        H = [input().rstrip() for _ in range(n)]
        R = [input().rstrip() for _ in range(n)]
        C = [input().rstrip() for _ in range(n)]

        # 🗝️H, R, C 모두 1인 좌표 (i, j, k)에 1 저장
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if H[j][k] == "1" and R[i][k] == "1" and C[i][j] == "1":
                        arr[i][j][k] = 1
        
        # 만든 arr을 기준으로 H, R, C를 하나씩 체크
        # 1. H 확인
        for j in range(n):
            for k in range(n):
                if H[j][k] == "1":
                    # 만약 (i, j, k) = 1인 좌표가 하나도 없다면, H 조건을 만족하지 못한 것.
                    if all(arr[i][j][k] != 1 for i in range(n)):
                        print("NO")
                        return
        
        # 2. R 확인
        for i in range(n):
            for k in range(n):
                if R[i][k] == "1":
                    if all(arr[i][j][k] != 1 for j in range(n)):
                        print("NO")
                        return
        
        # 3. C 확인
        for i in range(n):
            for j in range(n):
                if C[i][j] == "1":
                    if all(arr[i][j][k] != 1 for k in range(n)):
                        print("NO")
                        return
        
        # 조건을 모두 만족했다면 arr 출력
        print("YES")

        for i in range(n):
            for j in range(n):
                print(*arr[i][j], sep="")
    
    
    check(n)


main()


# 2) 최소한만 채워넣는 방식
# 조건을 만족하는 만큼만 채워넣는 방식이다.

# + 최소 해를 기반으로 추가로 채워넣으려면?
# -> arr이 1이고, M이 0인 곳을 찾아 채워넣으면 된다.

# 메모리: 49860KB / 시간: 520ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())

    def check(n):
        # 후보 칸들을 저장할 리스트
        arr = [[[0] * n for _ in range(n)] for _ in range(n)]

        H = [input().rstrip() for _ in range(n)]
        R = [input().rstrip() for _ in range(n)]
        C = [input().rstrip() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if H[j][k] == "1" and R[i][k] == "1" and C[i][j] == "1":
                        arr[i][j][k] = 1
        
        # 최종 결과값을 저장할 리스트
        M = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        # 1. H 만족
        for j in range(n):
            for k in range(n):
                # H = 1이고, arr(i, j, k)가 1이라면 채워넣음.
                if H[j][k] == "1":
                    for i in range(n):
                        if arr[i][j][k] == 1:
                            M[i][j][k] = 1
                            break
                    # H = 1인데 arr(i, j, k)가 모두 0이라면 M을 만들 수 없음!
                    else:
                        print("NO")
                        return
        
        # 2. R 만족
        for i in range(n):
            for k in range(n):
                if R[i][k] == "1":
                    # 이미 만족했다면 넘어감
                    if any(M[i][j][k] for j in range(n)):
                        continue
                    # 아니라면 R = 1, arr(i, j, k) = 1인 경우를 찾아서 채워넣음
                    for j in range(n):
                        if arr[i][j][k] == 1:
                            M[i][j][k] = 1
                            break
                    else:
                        print("NO")
                        return
        
        # 3. C 만족
        for i in range(n):
            for j in range(n):
                if C[i][j] == "1":
                    if any(M[i][j][k] for k in range(n)):
                        continue
                    for k in range(n):
                        if arr[i][j][k] == 1:
                            M[i][j][k] = 1
                            break
                    else:
                        print("NO")
                        return
        
        print("YES")
        for i in range(n):
            for j in range(n):
                print(*M[i][j], sep="")
    
    
    check(n)


main()