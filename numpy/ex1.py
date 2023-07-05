import numpy as np

# 행벡터 생성
age = np.array([60,70,12])
age

# 열벡터 생성
abc = np.array([[60],[70],[12]])
abc

# 행렬 생성
num = np.array([[1,2],[3,4]])
num

# 함수 arrange()
age = np.arange(1,6)
age

# 배열 원소 0, 1, 임의의 수로 채우기
age = np.zeros((2,3))
age

age_one = np.ones(5)
age_one

age_random = np.random.rand(2,2)
age_random

# 배열 사칙연산 (더하기, add())
temp1 = np.array([[1,2],[3,4]])
temp2 = np.array([[1,1],[1,1]])
temp1 + temp2
np.add(temp1,temp2)

# 배열 사칙연산 (뺄셈, subtract())
temp1-temp2
np.subtract(temp1, temp2)

# 배열 사칙연산 (곱셈, multiply())
temp3 = np.array([[1,2],[3,4],[5,6]])
temp4 = np.array([[2,2],[2,2],[3,4]])
temp3 * temp4
np.multiply(temp3,temp4)

# 배열 사칙연산 (나누기, divide())
temp3/temp4
np.divide(temp3,temp4)

# 벡터의 곱 (결과는 스칼라)
temp1 = np.array([1,2,3])
temp2 = np.array([[4],[5],[6]])
temp1.dot(temp2)
temp1
temp2

# 행렬의 곱 (결과는 행렬)
temp1 = np.array([[1,2,3],[4,5,6]])
temp2 = np.array([[1,2],[3,4],[5,6]])
temp1.dot(temp2)
temp1
temp2

temp1 = np.array([[3,6,9],[1,3,5]])
temp2 = np.array([[3,2],[3,1],[6,6]])
temp1.dot(temp2)
temp1
temp2

temp2.dot(temp1)

# 통계 함수 sum() - 배열 원소의 합계
temp1 = np.array([[1,2,3],[4,5,6]])
temp1
np.sum(temp1)

# 통계 함수 sum() - 배열 원소의 합계(행의 원소 합계: 옵션 'axis=0')
np.sum(temp1, axis=0)

# 통계 함수 sum() - 배열 원소의 합계(열의 원소 합계: 옵션 'axis=1')
np.sum(temp1, axis=1)

# 통계 함수 mean()
np.mean(temp1, axis=0)

# 통계 함수 mean()
np.mean(temp1, axis=1)

# 통계함수 median()
np.median(temp1)

temp2 = np.array([[1,2,3],[4,5,6],[4,5,6]])
np.median(temp1)

# 통계함수 max()
temp1 = np.array([[1,2,3],[4,5,6]])
np.max(temp1)
np.min(temp1)

# 통계함수 최소값 : 최대/최소값 인덱스
temp3 = np.array([[3,4,5],[6,7,8],[8,9,0]])
np.argmax(temp3)
np.argmin(temp3)

# 배열 조건 검색 any()
obj = np.array([[ 1.9, -0.2, -1, -3, -4 ]
                ,[ 2, 3, 4, 5, -1.8 ]
                ,[ -2.3, 3.5, 6, -7, -3 ]])
np.any(obj>0)
np.any(obj==0)
np.any(obj<0)

# 배열 조건 검색 all(), where()
obj = np.array([[ 1.9, -0.2, -1, -3, -4 ]
                ,[ 2, 3, 4, 5, -1.8 ]
                ,[ -2.3, 3.5, 6, -7, -3 ]])
# all()
np.all(obj>0)
np.all(obj==0)
np.all(obj<0)

obj = np.array([[ 1.9, -0.2, -1, -3, -4 ]
                ,[ 2, 3, 4, 5, -1.8 ]
                ,[ -2.3, 3.5, 6, -7, -3 ]])
# where()
np.where(obj<0, obj, 0)

# 배열의 모양 변경
abc = np.array([[1,2,3]])
abc

abc.reshape(1,3)
edf = np.array([[1,2,3,4], [4,5,6,7]])
edf
edf.reshape(4,2)

# 배열 arange() 함수 이용
np.arange(9)
np.arange(8).reshape(4,2)
np.arange(9).reshape(3,3)



