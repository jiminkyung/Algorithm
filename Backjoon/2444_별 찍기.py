# 별 뒤쪽은 공백이 없어야한다.
N = int(input())

for i in range(2*N-1):
    blank = abs(N-(i+1))
    if i < N:
        star = i*2+1
    else:
        star = 2*N - (blank*2+1)
    print(" "*blank + "*"*star)


# min()을 써도 가능. 이게 4ms 더 빠르다.
N = int(input())

for i in range(2*N-1):
    blank = abs(N-(i+1))
    star = min(i*2+1, 2*N - (blank*2+1))
    print(" "*blank + "*"*star)