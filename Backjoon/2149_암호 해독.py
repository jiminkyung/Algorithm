# 구현
# 문자열
# 정렬


# 문제: https://www.acmicpc.net/problem/2149

# 정렬 문제로 괜찮은듯? 나중에 다시 풀어볼만함
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    key = [(k, i) for i, k in enumerate(input().rstrip())]
    # key_idx[x]: x번째 값의 정렬 전 원래 위치
    key_idx = [idx for _, idx in sorted(key)]

    data = input().rstrip()

    # 주어지는 data는 열 기준으로 분리되어있으므로, 열의 크기별로 잘라야 함.
    col_size = len(data) // len(key)
    # words: (인덱스 x, x번째 열 데이터).
        # 사실상 words에 저장된 인덱스 x 데이터는 편하게 정렬하기 위함임.
        # words의 정렬 기준은 "현재 x번째 단어가 정렬 전 순서값".
    words = [(i//col_size, data[i:i+col_size]) for i in range(0, len(data), col_size)]
    words.sort(key=lambda x: key_idx[x[0]])

    # 열 기준 데이터들을 행 기준으로 연결시켜준 뒤 출력
    ret = list(zip(*(word[1] for word in words)))
    print("".join(map("".join, ret)))


main()


# words를 직접 정렬하는 대신, 아래와 같이 간접적으로 정렬해줄수도 있음.
def case_1():
    key = [(k, i) for i, k in enumerate(input().rstrip())]
    key_idx = [idx for _, idx in sorted(key)]

    data = input().rstrip()

    col_size = len(data) // len(key)
    words = [data[i:i+col_size] for i in range(0, len(data), col_size)]
    new_words = []

    for i in range(len(key)):
        word = words[key_idx.index(i)]
        new_words.append(word)
    
    ret = list(zip(*new_words))
    print("".join(map("".join, ret)))