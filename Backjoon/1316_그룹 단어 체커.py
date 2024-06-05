# 메모리: 31120KB / 시간: 48ms
N = int(input())

ret = 0

for _ in range(N):
    word = input()
    passed = []
    
    ret += 1
    for w in word:
        if w in passed and passed[-1] != w:
            ret -= 1
            break
        passed.append(w)

print(ret)


# 실행시간 줄여보기. 44ms
N = int(input())

ret = 0

for _ in range(N):
    word = input()
    passed = set()
    prev = ""
    
    is_True = True
    for w in word:
        if w in passed and prev != w:
            is_True = False
            break
        passed.add(w)
        prev = w

    if is_True:
        ret += 1

print(ret)