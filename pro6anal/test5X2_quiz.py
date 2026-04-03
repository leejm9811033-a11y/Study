# t-test 조건에 따른 가설검정 방법  https://nittaku.tistory.com/459
# anova 조건에 따른 가설검정 방법  https://velog.io/@pyose95/Data-Analysis

# * 통계적 가설검정 *
# --------------------------------------------------------------------------------------------
# * 카이제곱 검정
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

import pandas as pd
import scipy.stats as stats

# 데이터 로드
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")

# level, pass 열에 NA 행 제외
df_clean = df.dropna(subset=['level', 'pass'])
print(df_clean.head())
print(df_clean['level'].unique())   # [1. 2. 3.]
print(df_clean['pass'].unique())    # [2. 1.]
print()
ctab = pd.crosstab(index=df_clean['level'], columns=df_clean['pass'])
print(ctab)

chi2, p, dof, expected = stats.chi2_contingency(ctab)

print(f"\n카이제곱: {chi2}")    # 카이제곱: 2.7669512025956684
print(f"p-value: {p}")          # p-value: 0.25070568406521365

if p < 0.05:
    print(f"판정: p-value({p}) < 0.05 이므로 귀무가설을 기각 => 통계적으로 유의미")
else:
    print(f"판정: p-value({p}) >= 0.05 이므로 귀무가설을 채택 => 통계적 관련 없음")


# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'db': 'test',
    'port': 3306,
    'charset': 'utf8'
}

conn = pymysql.connect(**config)
query = "SELECT jikwonjik, jikwonpay FROM jikwon"
data = pd.read_sql(query, conn)
conn.close()

# NA 행 제외
df_jikwon = data.dropna(subset=['jikwonjik', 'jikwonpay'])

# (조건: 1000~2999:1, 3000~4999:2, 5000~6999:3, 7000~:4)
bins = [1000, 3000, 5000, 7000, 1000000] 
labels = [1, 2, 3, 4]
df_jikwon['pay_group'] = pd.cut(df_jikwon['jikwonpay'], bins=bins, labels=labels, right=False)

ctab_jik = pd.crosstab(index=df_jikwon['jikwonjik'], columns=df_jikwon['pay_group'])
chi2, p, dof, expected = stats.chi2_contingency(ctab_jik)

print(f"카이제곱: {chi2}")          # 카이제곱 : 37.40349394195548
print(f"p-value: {p}")              # p-value : 0.00019211533885350577

if p < 0.05:
    print(f"판정: p-value({p}) < 0.05 이므로 귀무가설을 기각 => 통계적으로 유의미")
else:
    print(f"판정: p-value({p}) >= 0.05 이므로 귀무가설을 채택 => 통계적 관련 없음")




