# 재귀
# AI선생님의 도움을 받아 작성한 풀이. 재귀 연습이 필요하다.
# 메모리: 35868KB / 시간: 88ms

def print_stars(n):
    if n == 1:
        return ["*"]
    
    stars = print_stars(n // 3)
    result = []
    
    for star in stars:
        result.append(star * 3)
    for star in stars:
        result.append(star + " " * (n // 3) + star)
    for star in stars:
        result.append(star * 3)
    
    return result

N = int(input())
pattern = print_stars(N)
print(*pattern, sep="\n")