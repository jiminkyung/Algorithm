# 수학
# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/1769
# 메모리: 34368KB / 시간: 108ms
from sys import stdin


input = stdin.readline

def main():
    X = input().rstrip()
    cnt = 0

    while len(X) > 1:
        X = str(sum(map(int, X)))  # 정수형으로 변환 -> sum -> 문자열로 변환
        cnt += 1

    print(cnt)
    print("YES" if int(X) % 3 == 0 else "NO")


main()


# 효율적인 코드. 바이너리 모드로 입력받고 ASCII 값으로 계산함.
# 출처👉 https://www.acmicpc.net/source/88481277
n = open(0, "rb").read().rstrip()
t = 0
c = sum(n) - (len(n) * 48)
while 1:
    if c < 10:
        print(f'{t}\n{"NO" if c%3 else "YES"}')
        break
    else:
        c = sum(n) - (len(n) * 48)
        n = str(c).encode()  # 바이너리 코드로 변환
        t += 1

"""
'0' → ASCII 48 → 실제 값 0 (48 - 48 = 0)
'1' → ASCII 49 → 실제 값 1 (49 - 48 = 1)  
'2' → ASCII 50 → 실제 값 2 (50 - 48 = 2)
'3' → ASCII 51 → 실제 값 3 (51 - 48 = 3)
'4' → ASCII 52 → 실제 값 4 (52 - 48 = 4)
...
이므로 48 * (숫자갯수)만큼을 빼 줌.
"""