# 아스키코드 잘 몰라서 검색해보고 풀었다.
# A-Z: 65~90, a-z: 97~122
# 대문자는 0~25 소문자는 26~51 => 0~51인덱스 총 52개의 배열
def solution(my_string):
    result = [0] * 52
    for i in my_string:
        if i.isupper():
            x = 65
        else:
            x = 71
        result[ord(i) - x] += 1
    return result