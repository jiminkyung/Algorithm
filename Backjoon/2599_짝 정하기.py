# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2599

# 방정식으로 풀었으나 간단한 풀이 발견함👉 https://www.acmicpc.net/source/49637877
# -> 반례가 여러개 나오는걸보니 현재는 통과되지 않을듯?

# 구현 문제 풀이시 다시 풀어볼만한 문제.
# 메모리: 32412KB / 시간: 84ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    students = [tuple(map(int, input().split())) for _ in range(3)]
    boys, girls = list(map(list, zip(*students)))

    # 만약 전체 남학생 수와 전체 여학생 수가 다르다면 짝 불가능.
    # 또는 x반 남학생 수가 x반을 제외한 여학생 수보다 많으면 불가능.
    if sum(boys) != sum(girls) or any(boys[i] > sum(girls) - girls[i] for i in range(3)):
        print(0)
        return
    
    print(1)
    """
    방정식을 세워보면,
    am = ab + ac / bm = ba + bc / cm = ca + cb
    af = ba + ca / bf = ab + cb / cf = ac + bc

    여기서 ab조합을 미리 구한 뒤 식을 사용해서 나머지 조합들(ac, ba, bc, ca, cb)를 구하는거임.
    a남b여 조합 수는 a반 남학생, b반 여학생보다 클 수 없으므로,
    ab 값 = a반 남학생 수, b반 여학생 수 중 더 작은 값으로 설정.
    """
    for ab in range(min(boys[0], girls[1]) + 1):
        ac = boys[0] - ab
        cb = girls[1] - ab
        bc = girls[2] - ac
        ba = boys[1] - bc
        ca = boys[2] - cb

        comb = [ab, ac, ba, bc, ca, bc]
        # 음수가 되면 불가능한 조합
        if any(c < 0 for c in comb):
            continue

        print(ab, ac)
        print(ba, bc)
        print(ca, cb)
        break


main()