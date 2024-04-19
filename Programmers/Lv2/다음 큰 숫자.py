def solution(n):
    cnt = bin(n).count("1")
    while True:
        n += 1
        num = bin(n)
        if num.count("1") == cnt:
            break
    return n

# 다른 사람의 풀이도 내 풀이와 비슷하다.