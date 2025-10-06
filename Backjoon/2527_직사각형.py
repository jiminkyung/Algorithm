# 기하학
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/2527

# 조건 체크를 명확하게 해야함.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    
    def check(coord):
        x1, y1, p1, q1, x2, y2, p2, q2 = coord

        # 더 왼쪽에 있는 도형을 1로 설정
        if x1 > x2:
            x1, y1, p1, q1, x2, y2, p2, q2 = x2, y2, p2, q2, x1, y1, p1, q1
        
        # 1. 꼭짓점 만나는지부터 체크
        if (p1, q1) == (x2, y2) or (p1, y1) == (x2, q2):
            return "c"
        
        # 2. 선분
        # x가 겹칠경우
        if p1 == x2:
            if y1 <= y2 <= q1 or y1 <= q2 <= q1 or (y2 < y1 < q2 and y2 < q1 < q2):
                return "b"
        # y가 겹칠경우
        if y1 == q2 or q1 == y2:
            if x1 <= x2 <= p1:
                return "b"
        
        # 3. 면
        if x1 <= x2 <= p1:
            if (y1 <= y2 <= q1) or (y1 <= q2 <= q1) or (y2 <= y1 <= q2 and y2 <= q1 <= q2):
                return "a"
        return "d"
    

    for _ in range(4):
        coord = list(map(int, input().split()))
        print(check(coord))


main()