def solution(arr):
    count = 0
    while True:
        temp = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        if temp == arr:
            break
        count += 1
    return count

# AI선생님의 도움을 받았다^^*