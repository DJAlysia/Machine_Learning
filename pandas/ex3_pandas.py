# pandas 시리즈 생성
import pandas as pd

# 리스트 전달하여 시리즈 생성
# ()안의 [] 는 python 리스트이고, 인덱스 리스트 생략하면 0부터 시작하는 정수형으로 생성

obj = pd.Series([60,70,12],['A','B','C'])
obj

obj2 = pd.Series({'a':60, 'b':70, 'c':80})
obj2

obj3 = pd.Series([60,70,12])
obj3

# pandas 시리즈 연산 주의 사항
obj4 = pd.Series([60,70,12],['A','B','C'])
obj5 = pd.Series([45,82,78],['D','A','B'])
obj4 + obj5

# pandas 데이터프레임 생성(2차원 배열 이용)
obj6 = pd.DataFrame([
    [60,3.8,4.4,'S'],
    [70,7.2,6.7,'A'],
    [12,6.3,5.9,'B']], index=['S','A','B'], columns=['age','weight','height','nickname']
                    )
obj6

obj7 = pd.DataFrame([
                    [45, 1.1, 6.5, 'Bam'],
                    [55, 3.6, 2.3, 'Boo'],
                    [65, 2.7, 3.1, 'Sam']], index=['1','2','3'], columns=['age','weight','height','name']
                    )
obj7

# pandas 데이터프레임 생성(시리즈 이용)
a = pd.Series([45, 1.1, 6.5, 'sol'], index=['age','weight','height','nickname'])
b = pd.Series([70, 1.1, 6.5, 'sin'], index=['age','weight','height','nickname'])
c = pd.Series([89, 1.1, 6.5, 'sam'], index=['age','weight','height','nickname'])

obj = pd.DataFrame([a,b,c],index=['grandpa','grandma','grandson'])
obj

# pandas 데이터프레임 생성(딕셔너리 이용)
# 딕셔너리로 데이터프레임을 생성하려면 딕셔너리 키가 속성명(칼럼명)이 되고 리스트의 요소가 열이 됨
dic = {'age':[45, 56, 87], 'weight':[3.4,7.3,4.5],'height':[5.5,6.6,7.7],
       'nickname':['S','A','F']}
obj = pd.DataFrame(dic, ['grandpa','grandma','grandson'])
obj


# pandas 데이터프레임(데이터 접근)
dic = {'age':[45, 56, 87], 'weight':[3.4,7.3,4.5],'height':[5.5,6.6,7.7],
       'nickname':['S','A','F']}
obj = pd.DataFrame(dic,['grandpa','grandma','grandson'])
obj
obj['nickname']
obj['age']

# pandas 데이터프레임(데이터 접근 오류)
dic = {'age':[45, 56, 87], 'weight':[3.4,7.3,4.5],'height':[5.5,6.6,7.7],
       'nickname':['S','A','F']}
obj = pd.DataFrame(dic,['grandpa','grandma','grandson'])
 # 한 개의 칼럼을 시리즈로 출력
obj['nickname','age']   # 오류(1개의 컬럼만 가능)
 
# pandas 데이터프레임(여러 개 가져올 때 [] 리스트 형)
dic2 = {'age':[45, 56, 87], 'weight':[3.4,7.3,4.5],'height':[5.5,6.6,7.7],
       'nickname':['S','A','F']}
obj2 = pd.DataFrame(dic,['grandpa','grandma','grandson'])
 # 여러 개의 칼럼을 시리즈로 출력
obj2[['nickname','age','height','weight','age','height']] 
 
 
# 데이터프레임 : 행 단위 접근
import pandas as pd
dic3 = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
dic3
obj = pd.DataFrame(dic3, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
obj
obj.loc['ppab']

# 데이터 프레임 : 행 단위 접근 2
dic4 = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
obj = pd.DataFrame(dic3, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
obj.loc[['ppab','ppac']]

# 데이터 프레임 : 행 단위 접근 3
dic5 = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
obj = pd.DataFrame(dic5, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
obj.iloc[[2,2],[1,2]]

# 데이터 프레임 다루기 (열 추가)
dic6 = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
obj = pd.DataFrame(dic6, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
 
 # 성별 추가
obj['sex']=['M','F','M','F','M','F']
obj
 
# 데이터 프레임 다루기 (열 추가 insert() 함수)
dic = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
obj = pd.DataFrame(dic, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
obj
 
 # 성별 추가(insert)
obj.insert(3, 'sex',['M','F','M','F','F','M'])
obj
 
newdic = {'A':1}
newdic['B'] = 2
newdic['C'] = 3
newdic
print(newdic['B'])
 
# 데이터 프레임 다루기 (행 추가 loc[])
dic = {
    'age' : [60,70,80,90,13,17],
    'weight' : [4.5,6.6,7.7,6.6,4.4,3.2],
    'height' : [5.4,6.7,3.2,4.1,4.3,2.9],
    'nickname' : ['S','A','F','G','H','E']
}
obj = pd.DataFrame(dic, index=['ppap','ppab','ppac','ppcc','ppdd','ppce'])
obj.loc['ppee']=[35,8.2,4.5,'C']
obj


