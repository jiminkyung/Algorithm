"""
비트 연산 문제.
첫번째 풀이는 내 풀이인데, 무식하게 하나하나 계산하는 방식이다.

두번째 풀이는 짝수일경우 맨 마지막비트를 1로 변환 => 홀수,
홀수일경우 01인 부분을 찾아 10으로 변환해준다.
만약 01인 부분이 없다면 전체가 1이라는 소리이므로 1 + 길이만큼0 을 반환한다.
ex) 13 -> 1101 -> 1110(14), 15 -> 1111 -> 10000(16)
"""

# 첫번째 풀이. TC 10, 11 시간초과.
def solution(numbers):
    ret = []
    for number in numbers:
        n = number + 1
        while True:
            if bin(n^number).count("1") <= 2:
                ret.append(n)
                break
            n += 1
    return ret

# 수정한 풀이.
def solution(numbers):
    ret = []
    for number in numbers:
        if number % 2 == 0:
            ret.append(number + 1)
        else:
            binary = "0" + bin(number)[2:]
            idx = binary.rfind("01")
            if idx == -1:
                binary = "10" + binary[1:].replace("1", "0")
            else:
                binary = binary[:idx] + "10" + binary[idx+2:]
            ret.append(int(binary, 2))
    return ret

print(solution([2, 7]))