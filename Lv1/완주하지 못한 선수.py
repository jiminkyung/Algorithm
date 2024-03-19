# 효율성 통과 실패.
def solution(participant, completion):
    ret = ""
    p = sorted(participant)
    c = sorted(completion)
    for n in p:
        if n in c:
            c.remove(n)
        else:
            ret += n
    return ret

# 다른사람 코드 1 - 딕셔너리
def solution(participant, completion):
    dic1={i:0 for i in participant}
    dic2={i:0 for i in participant}

    for i in participant:
        dic1[i]+=1
    for i in completion:
        dic2[i]+=1

    for i in dic1:
        if dic1[i]-dic2[i]==1:
            return i
        
# 다른사람 코드 2 - sort 후 비교
def solution(participant, completion):

    # 정렬을 해주어 비교하기 쉽게 만들기
    # participant와 completion를 정렬했기에 같은 인덱스의 이름이 같으면 완주를 했다는 뜻입니다.
    # 같은 인덱스의 이름이 다르면 완주를 못한 사람이겠죠.
    participant.sort()
    completion.sort()

    # 정렬된 참가자 명단과 완주자 명단을 순서대로 비교합니다.
    for a, b in zip(participant, completion):

        # 같은 인덱스의 이름이 다르면 해당 참가자가 완주하지 못한 선수입니다.
        if a != b:
            return a

    # 만약 모든 비교가 완료되었을 때, 마지막 참가자가 완주하지 못한 선수입니다.
    # completion은 participant보다 길이가 1 작기 때문입니다.
    return participant[-1]
    출처: https://1ets-just-do-it.tistory.com/61 [파이썬은 신이야🔥🔥🔥:티스토리]