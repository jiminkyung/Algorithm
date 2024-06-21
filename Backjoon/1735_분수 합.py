# 약수, 배수와 소수 2단계
# 메모리: 31120KB / 시간: 40ms

from sys import stdin


input = stdin.readline

numer1, denom1 = map(int, input().split())
numer2, denom2 = map(int, input().split())

numer = numer1*denom2 + numer2*denom1
denom = denom1 * denom2

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

ret_gcd = gcd(numer, denom)

print(numer//ret_gcd, denom//ret_gcd)


# 숏코딩. 가독성은 떨어짐.
a,b,c,d=map(int,open(0).read().split())
e=f=b*d;g=h=a*d+b*c
while e:g,e=e,g%e
print(h//g,f//g)