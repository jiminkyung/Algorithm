# 처음 코드. 둘레를 '최대한' 크게 하라고 해서 두 변의 값-1 이 되게끔 했는데, 문제가 개떡같다.
# 삼각형의 조건(가장 긴 변 < 나머지 두 변의 합)을 만족하면 그대로 만들어야한다. 그럼 그렇게 쓰던가.
n = list(map(int, input().split()))

if len(set(n)) == 1:
    print(sum(n))
else:
    n_max = sum(n) - max(n)
    print(n_max + n_max-1)


# 수정한 코드.
n = list(map(int, input().split()))

if len(set(n)) == 1:
    print(sum(n))
else:
    n_max = max(n)
    n.remove(n_max)
    if sum(n) > n_max:
        print(sum(n) + n_max)
    else:
        print(sum(n)*2 - 1)