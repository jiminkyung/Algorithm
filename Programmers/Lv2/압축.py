def solution(msg):
    alphabet = {chr(i): i-64 for i in range(65, 91)}
    ret = []

    idx, k = 0, 1
    while idx < len(msg):
        while idx + k <= len(msg) and msg[idx:idx+k] in alphabet: # 사전에 존재할때까지만 반복
            k += 1

        ret.append(alphabet[msg[idx:idx+k-1]]) # 사전에 존재하는 부분까지만
        alphabet[msg[idx:idx+k]] = len(alphabet) + 1
        idx += k - 1
        k = 1
    return ret

# AI에게 좀 더 가독성 좋은 코드로 리팩토링 시켜봤다. 내 원래 코드가 나은듯?
def solution(msg):
    alphabet = {chr(i): i-64 for i in range(65, 91)}
    ret = []
    
    while msg:
        for k in range(1, len(msg)+1):
            if msg[:k] not in alphabet:
                alphabet[msg[:k]] = len(alphabet) + 1
                ret.append(alphabet[msg[:k-1]])
                msg = msg[k-1:]
                break
        else:
            ret.append(alphabet[msg])
            break
    
    return ret