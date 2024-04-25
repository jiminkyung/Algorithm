def solution(bin1, bin2):
    ret = int("0b" + bin1, 2) + int("0b" + bin2, 2)
    return bin(ret)[2:]