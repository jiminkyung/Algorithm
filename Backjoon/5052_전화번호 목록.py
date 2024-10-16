# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/5052

# 시간초과...
from sys import stdin
import re

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    is_True = True

    number = [input().rstrip() for _ in range(n)]
    full_number = " ".join(number)

    for num in number:
        p = re.compile(r"\b" + num + r"\w+\b")
        matches = p.findall(full_number)

        if matches:
            is_True = False
            break

    print("YES" if is_True else "NO")


# 훨씬 간단한 풀이를 발견했다!!!
# 정렬한 후 바로 다음 문자열만 체크하는 방식이다.
# => 해당되는 번호가 하나라도 있다면 "NO"인 문제이기 때문에, 바로 옆 문자열만 체크해줘도 됨.

# 아래는 해당 풀이를 참고해서 다시 작성한 코드다.
# 출처👉 https://www.acmicpc.net/board/view/29419

# 메모리: 31120KB / 시간: 116ms
from sys import stdin


input = stdin.readline

def solution():
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    numbers.sort()
    
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return False
    return True

t = int(input())

for _ in range(t):
    print("YES" if solution() else "NO")