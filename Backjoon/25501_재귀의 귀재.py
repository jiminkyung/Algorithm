# 재귀

# 메모리: 33076KB / 시간: 44ms
import sys


words = iter(sys.stdin.read().split())
next(words)

for word in words:
    length = len(word)

    if word == word[::-1]:
        print(1, length//2 + 1)
    else:
        front = word[:length//2]

        if length % 2 == 0:
            back = word[length//2:][::-1]
        else:
            back = word[length//2 + 1:][::-1]
        
        cnt = 1
        for i in range(length):
            if front[i] == back[i]:
                cnt += 1
            else:
                break
        
        print(0, cnt)


# 더 간결하게 만들어보기.
# back = word[-(length//2):]와 같이 작성하면 문자열 길이의 홀/짝을 구분하지 않아도 된다.
# 🔴 사이트에 제출 시 오답 처리됨. 이유는 모름. => 🔵 틀린부분이 나올경우 바로 break를 걸어줘야함.
import sys


words = iter(sys.stdin.read().split())
next(words)

for word in words:
    length = len(word)
    if word == word[::-1]:
        sys.stdout.write(f"1 {length//2 + 1}\n")
    else:
        front = word[:length//2]
        back = word[-(length//2):][::-1]
        cnt = sum(1 for a, b in zip(front, back) if a == b) + 1
        sys.stdout.write(f"0 {cnt}\n")


# 위의 코드에서 문제점 해결.
# next(제너레이터, default)를 이용, next()는 이터레이터의 첫번째 값만 반환하고 없을경우 default 반환.
# 메모리: 33076KB / 시간: 44ms
import sys


words = iter(sys.stdin.read().split())
next(words)

for word in words:
    length = len(word)
    if word == word[::-1]:
        sys.stdout.write(f"1 {length//2 + 1}\n")
    else:
        front = word[:length//2]
        back = word[-(length//2):][::-1]
        cnt = next((i + 1 for i, (a, b) in enumerate(zip(front, back)) if a != b), len(front) + 1)
        sys.stdout.write(f"0 {cnt}\n")