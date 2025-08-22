# 구현
# 자료 구조
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/2002

# 🚨굳이 이렇게 풀 필요가 없었다. 아래에 큐 활용 풀이 코드 추가함.
# 피지컬로 푼 문제... ㅋㅋㅋ 나중에 다시 확인하고 경각심을 가지도록...

# 메모리: 56540KB / 시간: 100ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    cars = [input().rstrip() for _ in range(N)]
    order = {cars[i]: set(cars[:i]) for i in range(N)}

    # 출구조사
    cnt = 0
    output = [input().rstrip() for _ in range(N)]

    for i, car in enumerate(output):
        if order[car] & set(output[:i]) != order[car]:
            cnt += 1
    
    print(cnt)


main()


# 🗝️큐 개념을 사용하면 굉장히 간단한 문제였음.
# 출처👉 https://www.acmicpc.net/source/86325635

# 빠져나오는 차량과 큐의 첫번째 값이 다르면 추월이 발생한것이므로 카운트.
# 추월 차량(빠져나온 차량)을 큐에서 제거.
import sys
input = sys.stdin.readline

n = int(input())
enter = [input().strip() for _ in range(n)]

count = 0
for _ in range(n):
    car = input().strip()
    if enter[0] != car:
        count += 1
    enter.remove(car)
print(count)