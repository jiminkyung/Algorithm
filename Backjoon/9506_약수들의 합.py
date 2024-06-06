# 메모리: 31120KB / 시간: 44ms

def measure(num):  # 약수들을 구하는 함수.
    numbers = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            numbers.add(i)
            numbers.add(num // i)

    numbers.remove(num)
    return sorted(numbers)

while True:
    n = int(input())
    
    if n == -1:
        break

    sorted_numbers = measure(n)

    if n == sum(sorted_numbers):
        print(f"{n} = ", end="")
        print(*[i for i in sorted_numbers], sep=" + ")
    else:
        print(f"{n} is NOT perfect.")