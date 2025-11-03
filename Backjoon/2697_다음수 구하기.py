# 그리디 알고리즘
# 문자열


# 문제: https://www.acmicpc.net/problem/2697

# 규칙만 파악하면 쉬운 문제.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    def check(A: str) -> str:
        # A를 구성하는 숫자로 만들 수 있는 가장 큰 수는 내림차순으로 정렬된 경우임. (ex: 98765)
        # 따라서 오른쪽부터 차례대로 검사.
        # 🗝️ 만약 현재값보다 왼쪽값이 더 작다면, 더 큰 수를 만들 수 있음. (ex: 98756에서 5 < 6)
        lst = list(A)
        # point: 오른쪽부터 검사했을 때, 내림차순 조건을 불만족하는 첫번째 값의 인덱스
        point = 0
        for i in range(len(lst)-2, -1, -1):
            if lst[i+1] > lst[i]:
                point = i
                break
        else:
            return "BIGGEST"
            
        # 132 -> 213
        # 223 -> 232

        # trade_point: point 뒤의 숫자들 중 point값과 바꿀 값의 인덱스
        trade_point = point+1
        for i in range(point+1, len(lst)):
            # point값보다는 크고, 후보값보다 작다면 후보값(trade_point) 갱신
            if lst[i] > lst[point] and lst[i] < lst[trade_point]:
                trade_point = i
        
        # point값과 후보값을 스왑해주고, 남은 숫자들은 정렬해준다.
        lst[point], lst[trade_point] = lst[trade_point], lst[point]
        ret = lst[:point+1] + sorted(lst[point+1:])

        return "".join(ret)


    T = int(input())

    for _ in range(T):
        A = input().rstrip()
        print(check(A))


main()