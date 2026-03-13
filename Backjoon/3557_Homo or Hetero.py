# 자료 구조
# 집합과 맵
# 해시를 사용한 집합과 맵
# 트리를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3557
# 메모리: 45504KB / 시간: 124ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())
    lst = {}

    same = 0  # 같은 수가 2개 이상 있는 경우. ex) [2, 2, 4, 4]면 same = 2
    ret = []

    for _ in range(n):
        cmd, num = input().rstrip().split()

        if cmd == "insert":
            lst[num] = lst.get(num, 0) + 1
            # 삽입 후 해당 숫자의 갯수가 2개가 된다면, 새로운 same이므로 카운트.
            if lst[num] == 2:
                same += 1
        else:
            lst[num] = lst.get(num, 1) - 1
            # 삭제 후 해당 숫자의 갯수가 1개라면, 더이상 same이 아니므로 감산.
            if lst[num] == 1:
                same -= 1
            # 정확히 0개가 된다면, 딕셔너리에서 삭제.
            if lst[num] == 0:
                del lst[num]
        
        # len(lst) = 서로 다른 숫자의 갯수
        if same and len(lst) >= 2:
            ret.append("both")
        elif not same and len(lst) <= 1:  # [1]이거나 []일때.
            ret.append("neither")
        elif same:
            ret.append("homo")
        else:
            ret.append("hetero")
    
    print(*ret, sep="\n")


main()