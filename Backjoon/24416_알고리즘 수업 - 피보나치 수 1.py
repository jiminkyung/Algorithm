# 동적 계획법 1
# 메모리: 31120KB / 시간: 48ms

# 수열의 값 = 실행횟수

n = int(open(0).readline())

arr = [0] * (n+1)
arr[0] = arr[1] = arr[2] = 1

def fibonacci(n):
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[i]

print(fibonacci(n), n-2)