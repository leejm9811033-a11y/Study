# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
# 수집된 자료 :  
# kind quantity
# 1 64
# 2 72
# 3 68
# 4 77
# 2 56
# 1 NaN
# 3 95
# 4 78
# 2 55
# 1 91
# 2 63
# 3 49
# 4 70
# 1 80
# 2 90
# 1 33
# 1 44
# 3 55
# 4 66
# 2 77

import pandas as pd
from scipy.stats import f_oneway

# 데이터프레임 생성
df = pd.DataFrame({
    'kind':[1,2,3,4,2,1,3,4,2,1,2,3,4,1,2,1,1,3,4,2],
    'quantity':[64,72,68,77,56,None,95,78,55,91,63,49,70,80,90,33,44,55,66,77]
})

# NaN을 quantity 평균으로 대체
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())

# 그룹별 데이터
g1 = df[df['kind'] == 1]['quantity']
g2 = df[df['kind'] == 2]['quantity']
g3 = df[df['kind'] == 3]['quantity']
g4 = df[df['kind'] == 4]['quantity']

# 일원분산분석
stat, pvalue = f_oneway(g1, g2, g3, g4)

print(df)
print('group means:')
print(df.groupby('kind')['quantity'].mean())
print('F-statistic:', stat)
print('p-value:', pvalue)

if pvalue < 0.05:
    print('유의한 차이 있음 -> 귀무가설 기각')
else:
    print('유의한 차이 없음 -> 귀무가설 기각 못함')


# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 
# 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

import pandas as pd
import MySQLdb
from scipy.stats import f_oneway

conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='123',
    db='test',
    charset='utf8'
)

sql = """
SELECT b.busername, j.jikwonpay
FROM jikwon j
JOIN buser b ON j.busernum = b.buserno
WHERE b.busername IN ('총무부', '영업부', '전산부', '관리부')
AND j.jikwonpay IS NOT NULL
"""

df = pd.read_sql(sql, conn)
conn.close()

print(df)
print(df.groupby('busername')['jikwonpay'].mean())

g1 = df[df['busername'] == '총무부']['jikwonpay']   # 부서이름 일치하면 월급 확인.
g2 = df[df['busername'] == '영업부']['jikwonpay']
g3 = df[df['busername'] == '전산부']['jikwonpay']
g4 = df[df['busername'] == '관리부']['jikwonpay']

stat, pvalue = f_oneway(g1, g2, g3, g4)     # f_oneway로 pvalue 계산

print('F값:', stat)
print('p값:', pvalue)

if pvalue < 0.05:
    print('부서별 평균 연봉에 유의한 차이가 있다.')
else:
    print('부서별 평균 연봉에 유의한 차이가 있다고 보기 어렵다.')






