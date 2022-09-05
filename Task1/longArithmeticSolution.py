import numba
from numba import  njit
from numba import prange
import time
import numpy as np
#import gmpy2

@njit(fastmath=True,nopython=True,cache=True)
def str_to_int(s):
    final_index, result = len(s) - 1, 0
    for i,v in enumerate(s):
        result += (ord(v) - 48) * (10 ** (final_index - i))
    return result

@njit(fastmath=True,nopython=True,cache=True)
def numbalong(stra:numba.typed.List,strb:numba.typed.List):
  stra=stra[::-1]
  strb=strb[::-1]
  maxlen = max(len(stra),len(strb))

  shift=0
  result=''
  for pos in prange(maxlen):
    if pos<len(stra):
      itema=str_to_int(stra[pos])
    else:
      itema= 0
    if pos<len(strb):
      itemb=str_to_int(strb[pos])
    else:
      itemb= 0
    tmp=itema+itemb+shift
    shift=tmp//10
    result+=str(tmp%10)
  
  if shift>0:
    result+='1'
  return numba.typed.List(result[::-1])

@njit(fastmath=True,nopython=True,cache=True)
def SUM(n:str):
  n=str_to_int(n)
  result=numba.typed.List('1')
  for i in range(2,n+1):
    result=numbalong(result,list(str(i)))
  return result


start=time.time()
SUM('10')
print(time.time()-start)