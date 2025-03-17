# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17136

# 일반적인 DFS 풀이도 잘 통과함.
# 하지만 비트마스킹을 사용하면 훨씬 빠르게 통과 가능...
# + 메모이제이션도 사용하면 200ms대에 통과 가능함.
# 나중에 메모이제이션 활용 코드도 다시 봐야할듯.

# 1) 내 풀이 (일반적인 DFS)
# 메모리: 32412KB / 시간: 2568ms
from sys import stdin


input = stdin.readline

def main():
    def putting(x, y, field: list, count: list, size: int) -> bool:
        # 해당 사이즈의 색종이를 다 썼거나, 색종이를 붙일경우 10x10 범위를 넘어가면 False
        if count[size] == 0:
            return False
        
        # x = 7, size = 3인경우 1-based로는 x = 8, 사이즈 3짜리 색종이를 붙인다면
        # 8, 9, 10 이므로 10x10 범위를 벗어나지 않음.
        # 그러므로 x, x+1, x+2... x+(size-1) 까지 더한값을 기준으로 체크하는것과 같음.
        if x + size > 10 or y + size > 10:
            return False
        
        # 반연에 x + i는 실제 좌표값을 나타내므로, 만약 x = 8, size = 3인경우
        # x + i는 8, 9, 10 이 된다. 1-based 기준으로는 9, 10, 11이 되는셈. 따라서 10x10 범위를 벗어나게 됨.
        for i in range(size):
            for j in range(size):
                if x + i >= 10 or y + j >= 10 or field[x+i][y+j] != 1:
                    return False
        
        for i in range(size):
            for j in range(size):
                field[x+i][y+j] = 0
        
        count[size] -= 1
        return True
    
    def dfs(field: list, count: list, used: int):
        """ 색종이 사이즈별로 DFS 실행 """
        nonlocal min_used

        if used >= min_used:  # 기존 최솟값보다 작거나 같다면 중단
            return

        found = False
        for i in range(10):
            for j in range(10):
                if field[i][j] == 1:
                    found = True
                    x, y = i, j
                    break
            if found:
                break
        
        # 붙여야 할 곳이 없다면 최솟값 갱신
        if not found:
            min_used = min(used, min_used)
            return
        
        # 사이즈별로 DFS 실행
        for size in range(1, 6):
            new_field = [line[:] for line in field]
            new_count = count[:]

            if putting(x, y, new_field, new_count, size):  # 해당 사이즈를 붙일 수 있다면 실행
                dfs(new_field, new_count, used+1)


    field = [list(map(int, input().split())) for _ in range(10)]
    count = [0, 5, 5, 5, 5, 5]
    min_used = 26  # 가능한 최대값은 5*5 = 25이므로
    dfs(field, count, 0)

    print(min_used if min_used != 26 else -1)


main()


# ⭐ 2) 비트마스킹을 사용한 풀이
# 참고한 코드👉 https://www.acmicpc.net/source/88131409
# 메모리: 32544KB / 시간: 408ms
from sys import stdin


input = stdin.readline

def main():
    field = [0] * 10

    for i in range(10):
        for j in map(int, input().split()):
            field[i] <<= 1
            if j == 1:
                field[i] += 1
    
    def dfs(field, count, used):
        nonlocal min_used

        if used >= min_used:
            return

        for i in range(10):
            if field[i]:
                x, y = i, field[i].bit_length()
                break
        else:
            min_used = used
            return
        
        for size in range(5, 0, -1):
            # y: x행에서 가장 왼쪽에 있는 1의 위치.
            # 예를들어 y가 3이라면, 행 x는 00000 00100 이렇게 구성되어있는거임.
            if count[size] > 0 and x+size < 11 and y >= size:
                # (1 << size)-1: size만큼의 연속된 1비트들 생성 (ex: if size = 3, 111)
                # y-size: 위에서 만든 1비트들을 y-size만큼 왼쪽으로 이동시킴
                # size = 3, y = 5라면 2만큼 왼쪽으로 옮겨줌. 111 => 11100
                # field는 00000 10000인 상태이므로 붙일 수 있는 환경을 만들어주는거임
                row = ((1 << size)-1) << y-size

                for i in range(size):
                    # 만약 사이즈 범위 내에 좌표가 0인 경우가 있다면 break
                    if field[x+i] & row != row:
                        break
                else:  # 채울 수 있으면 DFS
                    new_field = field[:]
                    new_count = count[:]
                    new_count[size] -= 1
                    for k in range(size):  # 검사했으면 0으로 바꿔줌(사이즈 범위 외의 비트값들은 그대로)
                        new_field[x+k] ^= row
                    dfs(new_field, new_count, used+1)


    min_used = 26
    count = [0, 5, 5, 5, 5, 5]
    dfs(field, count, 0)
    print(min_used if min_used != 26 else -1)


main()


# 3) 비트마스킹 + 메모이제이션을 사용한 풀이
# 출처👉 https://www.acmicpc.net/source/29978475
import sys
input = sys.stdin.readline

def checkcheck(r, c, count):
    global paper_count, failed
    if count >= paper_count:
        return
    
    if r == 10:
        if count < paper_count:
            paper_count = count
        return
    if c == 0:
        col_check = 0
        for i in range(10):
            if board[r][i]:
                col_check |= 1<<i
        
        if str(papers) in dp[r][col_check]:
            if dp[r][col_check][str(papers)] > count:
                dp[r][col_check][str(papers)] = count
            else:
                return
        else:
            dp[r][col_check][str(papers)] = count
            
    elif c == 10:
        checkcheck(r+1, 0, count)
        return
    
    marked = is_marked(r,c)
    if marked:
        for i in range(1, marked+1):
            if papers[i-1]>0:
                mark(r,c,i,0)
                papers[i-1]-=1
                checkcheck(r,c+i,count+1)
                mark(r,c,i,1)
                papers[i-1]+=1
            else:
                failed = True
    else:
        checkcheck(r,c+1,count)
    return


def is_marked(r,c):
    if board[r][c]:
        if r < 6 and c < 6:
            if sum([sum(board[r+i][c:c+5]) for i in range(5)]) == 25:
                return 5
        if r < 7 and c < 7:
            if sum([sum(board[r+i][c:c+4]) for i in range(4)]) == 16:
                return 4
        if r < 8 and c < 8:
            if sum([sum(board[r+i][c:c+3]) for i in range(3)]) == 9:
                return 3
        if r < 9 and c < 9:
            if sum([sum(board[r+i][c:c+2]) for i in range(2)]) == 4:
                return 2
        return 1
    else:
        return 0

def mark(r,c,size, flag):
    for dr in range(size):
        for dc in range(size):
            board[r+dr][c+dc] = flag


board = [list(map(int,input().split())) for _ in range(10)]
papers = [5,5,5,5,5]
dp = [[{} for _ in range(1024)] for _ in range(10)]
paper_count = 30
failed = False
checkcheck(0,0,0)
if paper_count == 30:
    paper_count = 0
if not paper_count and failed:
    print(-1)
else:
    print(paper_count)