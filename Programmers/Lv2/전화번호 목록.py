"""
해시 문제.

효율성 테스트 있음.
"""

# 첫번째 시도 실패. 효율성 테스트 3, 4에서 걸림.
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)

    while phone_book:
        p = phone_book.pop()
        for number in phone_book:
            if p == number[:len(p)]:
                return False
    return True

# 두번째 시도. 에서 고뇌하다가 AI의 도움을 받았다. 인접한 번호순으로 정렬하는 풀이.
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # if phone_book[i + 1].startswith(phone_book[i]):  # startswith를 사용하면 매우 편리함.
        if len(phone_book[i]) <= len(phone_book[i + 1]) and phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True

# 정석 풀이! 해시맵 사용.
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True