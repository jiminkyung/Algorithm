# 백트래킹
# 대칭성 => 시간초과, 메모이제이션 => 메모리초과.

# 퀸은 상하좌우+대각선 상으로 움직일 수 있음.
# 행 번호 차이 = 열 번호 차이 => 같은 대각선상에 위치.

# 시간초과! 왜?
N = int(open(0).readline())
boardline = [0] * N
ret = 0

def nqueen(curr):
    global ret
    if curr == N:
        ret += 1
        return

    for i in range(N):
        is_promising = True

        for j in range(curr):
            if boardline[j] == i or abs(curr-j) == abs(i - boardline[j]):
                is_promising = False
                break
        if is_promising:
            boardline[curr] = i
            nqueen(curr+1)

nqueen(0)
print(ret)


# 비트마스킹을 이용한 풀이. 매우 빠르다고 함.
# 메모리: 31120KB / 시간: 9368ms
def dfs(row, ld, rd, n):
    """
    row: 현재 행
    ld, rd: 퀸의 왼쪽 대각선, 오른쪽 대각선
    poss: 가능한 열의 위치 파악 (ex: 0110 => 두번째, 세번째 열 가능)
    bit: 가능한 열 중 가장 오른쪽에 위치한 열 선택(모든 가능한 위치 순차적으로 순회 예정)
    count: 현재 상태에서 찾은 해답의 수
    """
    if row == all_bits:
        return 1
    
    count = 0
    poss = all_bits & ~(row | ld | rd)  # row, ld, rd가 아닌 열 => 가능한 열
    
    while poss:
        bit = poss & -poss
        poss -= bit
        count += dfs(row | bit, (ld | bit) << 1, (rd | bit) >> 1, n)
    
    return count

N = int(open(0).readline())
all_bits = (1 << N) - 1  # N=4일때, 1 << 4 => 10000, -1을 하면 1111이 됨.
print(dfs(0, 0, 0, N))


# 실행시간 28ms 코드 ㅋㅋㅋ
print([1,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])