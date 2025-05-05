# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1251
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    base = input().rstrip()
    length = len(base)

    reversed_word = {}
    ret = []

    # 먼저 뒤집힌 상태들을 모두 저장해줌.
    for i in range(length):
        for j in range(i+1, length+1):
            word = base[i:j]

            if word in reversed_word:
                continue

            reversed_word[word] = word[::-1]
    
    # 세 단어로 나누어야하니 가능한 구간포인트는 두개.
    # => 0 ~ first-1 / first ~ second-1 / second ~ 끝
    # ex) "a b c d e" 일때, 첫번째 구간포인트의 최대 범위는 5-2 = 3idx, 두번째는 5-1 = 4idx
    # 나눈 구간에 해당되는 단어들을 뒤집은 후 합체시켜야 하므로,
    # reversed_word에 저장해놓은 값을 가져와 더한 뒤 결과 리스트에 추가한다.
    for first in range(1, length-1):
        word_1 = reversed_word[base[:first]]
        for second in range(first+1, length):
            word_2 = reversed_word[base[first:second]]
            word_3 = reversed_word[base[second:]]

            ret.append(word_1 + word_2 + word_3)
    
    # 정렬 후 첫번째 단어 출력
    ret.sort()

    print(ret[0])


main()