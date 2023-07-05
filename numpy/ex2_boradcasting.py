# Numpy 브로드캐스팅(boradcasting)
# - 브로드캐스팅 의미 : 일정 조건만 맞으면 서로 다른 모양의 배열끼리 연산할 수 있도록 하는 기능
# - 브로드캐스팅의 조건
#   1. 한 배열의 차원이 1일 때
#   2. 첫 번째 배열의 행의 개수와 두 번째 배열의 열의 개수가 같을 때

# Numpy 브로드캐스팅(broadcasting) 유형 1

from numpy.core.multiarray import array
obj = array([[1,2,3]])
obj_result=obj+1
obj_result

# Numpy 브로드캐스팅(broadcasting) 유형 2
import numpy as np
obj = np.arange(9).reshape(3,3)+ np.arange(3)
obj

# Numpy 브로드캐스팅(broadcasting) 유형 3
import numpy as np
obj=np.array([[1,2,3]])
obj.reshape(3,1) + np.arange(3)
obj