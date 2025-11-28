# 수학
# 구현
# 브루트포스 알고리즘
# 정수론
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2859

# 실제 시간을 구할때에도 수식을 이용할 줄 알았는데, 그냥 브루트포스였음.
# 참고1: https://nahwasa.com/entry/%EC%9E%90%EB%B0%94-%EB%B0%B1%EC%A4%80-2859-%EB%B3%84-%EA%B4%80%EC%B0%B0-java
# 참고2: https://velog.io/@swany0509/%EB%B0%B1%EC%A4%80-%EB%B3%84%EA%B4%80%EC%B0%B0-2859

# 나중에 다시 풀어볼만한 문제

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    data = []

    for _ in range(4):
        hh, mm = map(int, input().rstrip().split(":"))
        curr = hh * 60 + mm
        data.append(curr)
    
    s1, s2, c1, c2 = data

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # 두 별의 위치 차이는 g 단위로만 발생함.
    # 그러므로 두 별의 시작위치 차이가 g로 나누어지지 않는다면, 두 별은 동시에 반짝일 수 없음.
    g = gcd(c1, c2)

    if abs(s2 - s1) % g:
        print("Never")
        return
    
    # 동시에 반짝이는 시간 찾기
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(100000000):
        # i: 첫번째 별 시간, j: 두번째 별 시간 이라고 할 때,
        # s1 + c1*i = s2 + c2*j를 만족하는 j가 자연수인지 확인.
        curr = s1 + c1*i - s2

        # curr >= 0: 두 번째 별이 시작한 이후
        # (curr = 0 인 경우는 첫번째 별의 반짝임이 두번째 별의 시작 시간과 정확히 일치할 때)
        # curr % c2 == 0: 두 번째 별의 주기로 나누어떨어짐 (j가 정수)
        if curr >= 0 and curr % c2 == 0:
            # 실제 시간 계산
            curr += s2  # s1 + c1*i - s2를 해줬으므로 다시 s2를 더해줌.

            day = curr // 1440  # 시간 // (60 * 24)
            print(days[day % 7])

            curr %= 1440
            hh, mm = curr // 60, curr % 60
            print(f"{hh:0>2}:{mm:0>2}")

            break


main()