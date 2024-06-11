# 브루트포스
# 메모리: 31120KB / 시간: 748ms
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break


# 근의 공식 활용. 40ms.
# 참고: https://velog.io/@gaeun23/python-Baekjoon-%EB%B0%B1%EC%A4%80-19532-%EC%88%98%ED%95%99%EC%9D%80-%EB%B9%84%EB%8C%80%EB%A9%B4%EA%B0%95%EC%9D%98%EC%9E%85%EB%8B%88%EB%8B%A4
a, b, c, d, e, f = map(int, input().split())

x = (e*c - b*f) // (a*e - d*b)
y = (a*f - d*c) // (a*e - d*b)
print(x, y)