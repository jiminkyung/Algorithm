def solution(n):
    start = i = 1
    ret = curr = 0
    while i <= n+1:
        if curr > n:
            curr -= start
            start += 1
        elif curr == n:
            ret += 1
            curr -= start
            start += 1
        else:
            curr += i
            i += 1
    return ret

# 공식을 이용한 한줄코드.
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

# for + while
def expressions(num):
    answer = 0
    for i in range(1, num+1):
        summ = 0
        while (summ < num):
            summ += i
            i += 1
        if summ == num:
            answer += 1
    return answer

# for + for, 정석코드.
def expressions(num):
    answer = 0
    for x in range(1,num+1):
        sum = 0
        for y in range(x, num+1):
            sum += y
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break

    return answer