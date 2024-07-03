# 재귀
# 참고: https://shoark7.github.io/programming/algorithm/tower-of-hanoi
# 메모리: 31120KB / 시간: 860ms

def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

N = int(input())
print(2**N-1)
hanoi(N, 1, 3, 2)


# 메모이제이션을 이용한 코드. 시간: 52ms
import sys
m={}
def h(n,s,a,e):
 k=(n,s,a,e)
 if k in m:
  return m[k]
 if n==1:
  return f'{s} {e}'
 else:
  m[k]='\n'.join([h(n-1,s,e,a),f'{s} {e}',h(n-1,a,s,e)])
  return m[k]
        
n=int(input())
sys.stdout.write(f'{2**n-1}\n')
sys.stdout.write(h(n,1,2,3))