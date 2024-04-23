"""
문제에서 H-index 설명을 잘 못했나보다. 난이도에 비해 질문글 수가 상당하다;;
아래는 질문탭에서 발견한 잘 설명된 글.
👉 https://school.programmers.co.kr/questions/64629
- 논문 n편 증, a번 이상 인용된 논문이 b편 이상이면 a 와 b중 작은 값이 hIndex 값입니다.
"""

def solution(citations):
    cnt = [min(len(list(filter(lambda x: x >= i, citations))), i) for i in citations]
    return max(cnt)