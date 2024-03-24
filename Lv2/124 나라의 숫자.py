# 3진법을 이용한다는것만 알아차리고 그 뒤론 삽질만 했다.
# 참고 https://hoons-dev.tistory.com/67
# 알고리즘 풀 땐 적어도 30분은 생각하자...

def solution(n):
    ret = ""
    while n:
        tmp = n % 3
        if not tmp:
            tmp = 4
            n -= 1
        ret = str(tmp) + ret
        n //= 3
    return ret

# 조만간 수학문제집 진짜 사야겠다. 논리적인 사고력이 심각하다.