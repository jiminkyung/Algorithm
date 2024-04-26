"""
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
"""

# 처음 답. 2/8/10/16 진수만 말하는줄 알았다.
def solution(n, t, m, p):
    base = {2: bin, 8: oct, 10: None, 16: hex}
    if n != 10:
        nums = "".join([base[n](i)[2:] for i in range(t*m)])
    else:
        nums = "".join(str(i) for i in range(t*m))
    ret = nums[p-1::m].upper()
    return ret[:t]

# 정답. 2~16까지 모든 진법. (다른분 코드 참고 - 문자열 뒤집는 타이밍)
def solution(n, t, m, p):
    alp = "0123456789ABCDEF"
    nums = "0"

    for i in range(t*m+1):
        tmp = ""
        while i:
            tmp += alp[i % n]
            i //= n
        nums += tmp[::-1]
    
    ret = nums[p-1::m]
    return ret[:t]