import numba
import numpy as np
from numba import  njit
from numba import prange
import time
import gmpy2

@njit(numba.types.uint64(numba.types.uint64),fastmath=True)
def mysum(number:numba.types.uint64)->numba.types.uint64:
  result=0
  for i in prange(1,number+1):
    result=np.add(result,i)
  return numba.types.float64(result)

def Sum(number):
  if number<=10**9:
    return mysum(number)
  else:
    return int(gmpy2.xmpz(number)*(gmpy2.xmpz(number)+1)/2)


cur_time=time.time()
print((Sum(10000000000000000000000000000)))
print(time.time()-cur_time)