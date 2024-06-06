# 처음에 문제 제대로 안읽고 짠 코드...^^ 제목부터가 '소인수분해'였는데.
N = int(input())

def measure(num):
    numbers = set()
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            numbers.add(i)
            numbers.add(num // i)
    return sorted(numbers, reverse=True)

measured = measure(N)
tmp = measured.pop()

while N > 1:
    if N % tmp != 0:
        tmp = measured.pop()
    N //= tmp
    print(tmp)


# 수정한 코드. 메모리: 31120KB / 시간: 44ms
N = int(input())

def factorize(num):
    # factor가 소수인지 아닌지는 굳이 확인하지 않아도 됨.
    factor = 2
    while factor <= int(num**0.5):
        if num % factor == 0:
            print(factor)
            num //= factor
        else:
            factor += 1

    if num > 1:  # 반복문이 끝난 후에도 num이 2 이상이라면, num이 소수라는 소리이므로 그대로 출력.
        print(num)

if N == 1:
    pass
else:
    factorize(N)