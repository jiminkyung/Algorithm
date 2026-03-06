# 구현
# 문자열
# 파싱


# 문제: https://www.acmicpc.net/problem/3518
# 메모리: 34456KB / 시간: 72ms
from sys import stdin


def main():
    data = stdin.read().splitlines()
    L = 0  # 가장 긴 문장의 길이 (각 문장이 몇개의 단어를 포함했는지, 포함갯수의 최댓값)
    words = []

    for line in data:
        word = line.split()

        if L < len(word):
            L = len(word)
        
        words.append(word)
    
    # length[i]: 각 문장에서의 i번째 단어의 길이 중 최대값
    length = [0] * L

    for i in range(L):  # i번째 단어
        max_len = 0
        for j in range(len(words)):  # j번째 문장
            if len(words[j]) <= i:
                continue
            
            if len(words[j][i]) > max_len:
                max_len = len(words[j][i])
        
        length[i] = max_len + 1  # 각 단어들을 공백으로 분리해줘야하므로 +1
    

    for word in words:
        ret = ""
        for i in range(len(word)-1):  # 마지막 단어 뒤에는 띄어쓰기 할 필요 X
            ret += word[i]
            ret += " " * (length[i] - len(word[i]))
        ret += word[-1]
        print(ret)


main()