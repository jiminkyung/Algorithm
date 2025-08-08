# 문제: https://www.acmicpc.net/problem/1900

# 정렬을 사용해서 풀거나 완전탐색으로 풀어야 하는 문제.

# 1) 정렬 사용 풀이
# 메모리: 34456KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    """
    경기력이 좋은 선수를 왼쪽에(앞에) 배치해야 한다.

    선수의 경기력을 T, 힘을 P, 링의 힘을 R이라고 했을때 식은 아래와 같음.
        T1 = P1 + P2*R

    1번 선수가 2번 선수를 이기려면, T1 > T2가 되어야함.
        P1 + P2*R1 > P2 + P1*R2
    이걸 P1, P2끼리 묶어주려면 항을 이동시켜줘야 함.
        P1 - P1*R2 > P2 - P2*R1 -> P1(1 - R2) > P2(1 - R1) -> (1 - R2)/P2 > (1 - R1)/P
    
    => T1 > T2가 되려면 (1 - R2)/P2 > (1 - R1)/P1이 되어야 한다.
    => 즉, (1 - R)/P의 값이 크면 클수록 경기력이 나쁘다는 얘기이므로, 오른쪽에 와야 한다.
    => 따라서 (1 - R)/P 크기순으로 오름차순 정렬하면 된다.
    """
    N = int(input())
    players = [tuple(map(int, input().split())) + (i+1,) for i in range(N)]
    players.sort(key=lambda x: (1 - x[1])/x[0])

    for i in range(N):
        print(players[i][2])


main()


# 2) 완전탐색 풀이 (PyPy3)
# 메모리: 112620KB / 시간: 1612KB
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    players = [tuple(map(int, input().split())) + (i,) for i in range(N)]  # 선수 번호는 따로 추가하지 않아도 될듯.
    winning = [0] * N

    for i in range(N):
        p1, r1, n1 = players[i]
        for j in range(i+1, N):
            p2, r2, n2 = players[j]

            if p1 + p2*r1 > p2 + p1*r2:
                winning[n1] += 1
            else:
                winning[n2] += 1
    
    # winning[번호] = 해당 번호의 승률 이므로 번호를 winning에 대입하여 내림차순 정렬.
    numbers = list(range(1, N+1))
    numbers.sort(key=lambda x: -winning[x-1])

    print(*numbers, sep="\n")


main()