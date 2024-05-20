"""
TC가 하나밖에 없어서 설명글을 참고했다. 👉 https://school.programmers.co.kr/questions/64956
설명글을 참고하자면, 너비와 높이값의 공약수가 존재하지 않을 경우 사용할 수 없는 직사각형의 수는 w + h - 1 과 같다.
하지만 TC와 같이(w: 8, h: 12) 공약수가 존재한다면, 두 수의 최대공약수를 기준으로 나눈 값을 기준으로 계산해야한다.
패턴이 반복되는 형태이기 때문이다. (설명글 참고)
즉 (8, 12) -> 4로 나눠 -> (2, 3)가 되고, (2+3-1)*4 -> 16 이 나오게 된다.
답은 8 * 12 - 16 = 80. 정답!
"""

def solution(w, h) -> int:
    """
    gcd(num1, num2): 최대공약수를 구하는 함수
    factor: 두 수의 최대공약수
    based_w,h: w,h를 최대공약수로 나눈 값. 패턴을 구하기 위한 기본값.
    excepted: 제외되는 직사각형의 수.
    """
    def gcd(num1, num2):
        if not num2:
            return num1
        return gcd(num2, num1 % num2)
    
    factor = gcd(w, h)
    based_w, based_h = w//factor, h//factor

    excepted = (based_w + based_h - 1) * factor
    return w * h - excepted