# 분할 정복

# 메모리: 69452KB / 시간: 4268

from sys import stdin


input = stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

ret = [0, 0, 0]

def checking_paper(row, col, size):
    default = paper[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != default:
                thirds = size // 3
                # 👇 함수 호출을 for문으로 돌리면 가독성이 좋아질듯
                # for r in range(row, row+size, thirds):
                #     for c in range(col, col+size, thirds):
                #         checking_paper(r, c, thirds)
                checking_paper(row, col, thirds)
                checking_paper(row+thirds, col, thirds)
                checking_paper(row+thirds*2, col, thirds)
                checking_paper(row, col+thirds, thirds)
                checking_paper(row, col+thirds*2, thirds)
                checking_paper(row+thirds, col+thirds, thirds)
                checking_paper(row+thirds, col+thirds*2, thirds)
                checking_paper(row+thirds*2, col+thirds, thirds)
                checking_paper(row+thirds*2, col+thirds*2, thirds)
                return
    
    ret[default] += 1

checking_paper(0, 0, N)
print(f"{ret[-1]}\n{ret[0]}\n{ret[1]}")


# 시간이 내 절반가량(2048ms)인 코드.
# size가 3이면서 같지 않을때, 함수를 호출하지 않고 for문으로 추가해줌.
import sys


def count_paper(size, x, y):
    global count
    start = paper[x][y]
    is_paper = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != start:
                is_paper = False
                break
        if not is_paper:
            break

    if is_paper:
        count[start] += 1
        return

    if size == 3:
        for i in range(x, x + size):
            for j in range(y, y + size):
                count[paper[i][j]] += 1
        return

    else:
        next_size = size // 3
        for i in range(x, x + size, next_size):
            for j in range(y, y + size, next_size):
                count_paper(next_size, i, j)


read = sys.stdin.readline
N = int(read())
paper = [list(read().split()) for _ in range(N)]
count = {'1': 0, '-1': 0, '0': 0}
if N == 1:
    count[paper[0][0]] = 1
else:
    count_paper(N, 0, 0)
print(count['-1'])
print(count['0'])
print(count['1'])