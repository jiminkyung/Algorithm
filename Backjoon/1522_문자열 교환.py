# 슬라이딩 윈도우
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1522

# 문제 조건이 명확하지 않아 헷갈렸음.
# 문제에서 말하는 교환 = word[i]와 word[j]를 swap
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    word = input().rstrip()
    # 단어 속 a의 갯수
    A = word.count("a")
    # a 길이만큼까지의 단어 속 b의 갯수
    B = sum(1 for i in range(A) if word[i] == "b")
    min_cnt = B

    # 원형이므로 단어 두개를 이어줌
    full_word = word + word
    
    # 🗝️a만큼의 단어 속 b의 갯수 = 교환해야 할 횟수 다.
    # a칸씩 체크. => 한 칸씩 옮겨가며 기존 값 갱신.

    # ex) baabbaa -> a의 갯수가 총 4개이므로 4칸씩 체크한다. 초기 B의 값은 2.
    # 인덱스를 한칸 옮겨 4번 인덱스 확인 -> b이므로 B += 1
    # 체크 범위에서 제외되는 0번 인덱스 확인 -> b이므로 B -= 1
    for i in range(len(word) - 1):
        if full_word[i] == "b":
            B -= 1
        if full_word[i + A] == "b":
            B += 1
        
        min_cnt = min(B, min_cnt)
    
    print(min_cnt)


main()