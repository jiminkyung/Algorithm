"""
클로드를 통한 풀이...

answer: 가장 짧은 경우의 길이. 초기값은 s의 길이로 설정.
step으로 압축단위를 설정. 1부터 s의 길이 절반까지.
- 최소한 문자 하나를 압축단위로 고려해야 하기 때문에 1부터 시작.
- 압축단위값이 문자열의 절반을 넘어가면 의미가 없음.
- 절반 표현을 len(s)//2+1로 설정한 이유 => 문자열이 홀수일 경우도 고려함.
compressed: 압축된 문자열을 저장할 변수.
prev: 이전에 압축한 문자열을 저장할 변수. 초기값은 문자열의 첫번째 압축 단위.
count: 동일한 문자열이 연속으로 나오는 횟수.
"""

def solution(s):
    answer = len(s)
    
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
        
    return answer