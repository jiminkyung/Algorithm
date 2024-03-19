# 이것도 역시 실습때 풀어봤었다.
# https://colab.research.google.com/drive/1L87Nl1nlPJzQoF5hFvDKqV7hS-tR-llV?usp=sharing#scrollTo=-n4pV-VBePvi

def solution(n, arr1, arr2):
    ret = []
    for i, j in zip(arr1, arr2):
        ret.append(bin(i | j)[2:].replace("1", "#").replace("0", " ").rjust(n, " "))
    return ret