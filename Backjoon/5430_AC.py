# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/5430
# 반례모음집👉 https://www.acmicpc.net/board/view/140389

# 메모리: 43080KB / 시간: 132ms
from sys import stdin
from collections import deque


input = stdin.readline

T = int(input())

for _ in range(T):
    try:
        p = input().rstrip()
        n = int(input())
        if n == 0:  # n이 0일때 아래처럼 생성하면 deque([''])로, 빈 문자열을 원소로 가진 덱이 형성됨.
            input()
            arr = deque([])
        else:
            arr = deque(list(input().rstrip()[1:-1].split(",")))
        rev = 1

        for cmd in p:
            if cmd == "R":  # R만큼 뒤집기
                rev *= -1
            else:
                if rev == 1:  # 뒤집히지 않은 상태라면 왼쪽에서, 뒤집혔다면 오른쪽에서 pop
                    arr.popleft()
                else:
                    arr.pop()
        if rev == -1:
            arr.reverse()
        print(f"[{','.join(arr)}]")  # 🚨안에는 작은 따옴표(or 작따 안에 큰따)로 작성해야 컴파일 에러가 발생하지 않음
    except:
        print("error")