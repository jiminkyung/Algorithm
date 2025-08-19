# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1985

# set 사용 문제
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    def check(x: str, y: str) -> str:
        A = list(map(int, x))
        B = list(map(int, y))

        A_set = set(A)
        B_set = set(B)

        # 기존 코드는,
        # len(A_set) == len(B_set) and A_set & B_set == A_set 이었음.
        # 🚨하지만 어차피 set은 순서가 상관 없기 때문에 A_set == B_set으로 간단하게 비교 가능.

        # 1. 구성 번호가 완전히 같다면 frineds
        if A_set == B_set:
            return "friends"
        
        # 2. 아니라면 하나씩 변환시켜가며 검사
        # +-, -+ 모두 체크
        for i in range(len(x)-1):
            # +- 의 경우
            A[i] += 1
            A[i+1] -= 1

            # 변환시킨 숫자가 0 ~ 9 사이라면 친구 확인
            if 0 <= A[i] <= 9 and 0 <= A[i+1] <= 9:
                # 여기도 마찬가지로 set(A) & B_set == B_set 으로 풀었으나 틀림.
                # 굳이 저렇게 풀려면 위에서처럼 len으로 비교해줘야함. 안전하게 == 을 사용하자.
                if set(A) == B_set:
                    return "almost friends"
            
            # -= 의 경우 (앞에서 +- 변환하였으니 2만큼 -+ 변환)
            A[i] -= 2
            A[i+1] += 2

            # 마찬가지로 0 ~ 9 사이라면 친구 확인
            if 0 <= A[i] <= 9 and 0 <= A[i+1] <= 9 and i != 0 or A[i] != 0:
                if set(A) == B_set:
                    return "almost friends"
            
            # 모두 만족하지 못했다면 원상복구
            A[i] += 1
            A[i+1] -= 1
        
        return "nothing"
    

    # 디지털 친구 검사
    for _ in range(3):
        x, y = input().rstrip().split()
        # 🚨각 정수를 기준으로 변환해봐야함. 한 정수로만 변환하면 친구여도 nothing이 나와버릴 수 있음.
        r1 = check(x, y)
        r2 = check(y, x)

        if r1 == "friends":
            print("friends")
        elif r1 == "almost friends" or r2 == "almost friends":
            print("almost friends")
        else:
            print("nothing")


main()