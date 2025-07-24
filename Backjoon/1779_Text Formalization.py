# 구현
# 문자열
# 파싱


# 문제: https://www.acmicpc.net/problem/1779

# Python3로도 통과 가능. 하지만 맞힌 사람 목록에 안 뜬다.
# 아마 PyPy3로 통과된 결과가 실제 결과일듯? PyPy로 제출했을때의 메모리와 Python일때의 메모리가 꽤 차이남...
# Python3 -> 메모리: 33432KB / 시간: 1848ms

# 메모리: 111456KB / 시간: 372ms (PyPy3)
from sys import stdin


input = stdin.readline

"""
조건이 애매해서 힘들었던 문제다. 통과된걸로보아 정확한 조건은 아래와 같을듯.
1. 동일한 문자열 기준 축약어 - 약어 순으로 매칭. 매칭되는 축약어가 없을때에만 약어 매칭을 시도한다.
2. (축약어) 변환 횟수 제한 X, (약어) 글 하나당 한번씩만 변환 가능.
3. 한 문장에 두 개 이상의 약어가 존재한다면 첫 번째로 나오는 약어만 변환.
4. 만약 문자열 안에 매칭되는 축약어/약어가 여러개 존재한다면, 가장 긴 부분이 매칭되는 축약어/약어로 변환.

처음엔 replace/re모듈을 사용했지만 실패!
🗝️문자열을 처음부터 끝까지 스캔해가며 매칭해야한다.
로직 자체는 쉽지만 조건 파악이 어려움. 다시 풀어볼만한 문제인듯?
"""
def check(lines: list[str], contraction: list[tuple], acronym: list[tuple]) -> list[str]:
    used = set()  # 사용한 약어들
    ret = []

    for line in lines:
        i = 0
        new_line = ""

        while i < len(line):
            found = None  # (바꿀 문자, 원본 문자열의 길이)
            longest = -1  # 매칭되는 문자 중 가장 긴 문자열의 길이

            # 1. 축약형 먼저 확인해야함 (contraction)
            for key, val, l in contraction:
                if i+l <= len(line) and line[i:i+l] == key:
                    if longest < l:
                        longest = l
                        found = (val, l)
            
            # 2. 없으면 약어 확인 (acronym)
            if not found:
                k = None
                for key, val, l in acronym:
                    if key in used:
                        continue
                    if i+l <= len(line) and line[i:i+l] == key:
                        if longest < l:
                            longest = l
                            found = (val, l)
                            k = key
                
                if found:  # 매칭되는 약어가 있다면 사용 체크
                    used.add(k)
            
            # 3. 매칭되는 축약어 or 약어가 있었다면 변환값 저장 후 변환값의 길이만큼 idx 증가
            if found:
                new_line += found[0]
                i += found[1]
            else:
                new_line += line[i]
                i += 1
            
        ret.append(new_line)
    return ret


def main():
    data = stdin.read().splitlines()
    N, M = map(int, data[0].split())

    # 축약어, 약어 저장
    contraction, acronym = [], []
    idx = 1

    for _ in range(N):
        word, new_word = data[idx].replace('"', "").split(" -> ")
        # 원본, 대문자, 첫글자만 대문자 순서대로 저장
        candidates = [(word, new_word, len(word)), (word.upper(), new_word.upper(), len(word)), (word.capitalize(), new_word.capitalize(), len(word))]
        contraction.extend(candidates)
        idx += 1
    
    for _ in range(M):
        word, new_word = data[idx].replace('"', "").split(" -> ")
        acronym.append((word, f"{new_word} ({word})", len(word)))
        idx += 1
    
    lines = []
    while idx < len(data):
        line = data[idx]
        idx += 1

        # 글의 끝부분에 도달하면 변환 후 출력
        if line == "#":
            ret = check(lines, contraction, acronym)
            for r in ret:
                print(r)
            print("#")
            lines = []
        else:
            lines.append(line)


main()