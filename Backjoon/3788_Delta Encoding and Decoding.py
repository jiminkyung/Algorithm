# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3788

# 입출력 형식에 신경써야하는 문제.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    data = stdin.read().splitlines()
    # code: {알파벳: 숫자}, rev_code: {숫자: 알파벳}
    code = {chr(i+65): i for i in range(26)}
    rev_code = {v: k for k, v in code.items()}

    for line in data:
        # 첫번째 공백 기준으로 명령어/문자 를 나눔.
        parts = line.split(maxsplit=1)
        cmd = parts[0].upper()
        words = parts[1] if len(parts) > 1 else ""  # 🚨 cmd만 존재하고 words는 존재하지 않을수도 있으므로 이렇게 처리해줘야함.

        # 1. 암호화
        if cmd == "ENCRYPT":
            ret = ""
            prev = "A"

            for i in range(len(words)):
                if words[i].isalpha():
                    # 암호화 시 -> (현재 평문 문자 - 이전 평문 문자) % 26
                    val = (code[words[i].upper()] - code[prev]) % 26
                    new_char = rev_code[val]
                    prev = words[i].upper()  # 이전값은 대문자로 기억해두기.
                    ret += new_char if words[i].isupper() else new_char.lower()
                else:
                    # words[i-1] 값이 알파벳이 아니었다면, prev를 다시 "A"로 설정.
                    prev = "A"
                    ret += words[i]
            
            print(f"RESULT:  {ret}")
        # 2. 복호화
        elif cmd == "DECRYPT":
            ret = ""
            prev = "A"

            for i in range(len(words)):
                if words[i].isalpha():
                    # 복호화 시 -> (현재 암호 문자 + 이전 평문 문자) % 26
                    # 평문을 P, 이전평문을 K, 암호문을 C 라고 했을 때,
                    # C = (P - K) % 26이므로, P = (C + K) % 26이 가능함. 따라서 암호문 C를 가지고 원래의 평문 P를 구할 수 있음.
                    val = (code[words[i].upper()] + code[prev]) % 26
                    org_char = rev_code[val]
                    prev = org_char
                    ret += org_char if words[i].isupper() else org_char.lower()
                else:
                    prev = "A"
                    ret += words[i]

            print(f"RESULT:  {ret}")
        # 3. 새로운 키 적용
        elif cmd == "CIPHER":
            new_code = "".join(words[i] for i in range(len(words)) if words[i].isalpha())
            new_code = new_code.upper()

            # 중복없이 26글자 모두 존재할경우에만 키 업데이트.
            if len(set(new_code)) == len(new_code) == 26:
                print(f"Good cipher.  Using {new_code}.")
                code = {new_code[i]: i for i in range(26)}
                rev_code = {v: k for k, v in code.items()}
            else:
                print("Bad cipher.  Using default.")
                code = {chr(i+65): i for i in range(26)}
                rev_code = {v: k for k, v in code.items()}
        # 4. 이상한 명령어가 주어질경우
        else:
            print("Command not understood.")


main()