# 원격 DB 연동 - jikwon 자료를 읽어 dataFrame에 저장
# import MySQLdb
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay
        from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    cursor.execute(sql)

    # for (jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay) in cursor:
    #     print(jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay)
    # DataFrame으로 출력

    df1 = pd.DataFrame(cursor.fetchall(),
                columns=['jikwonno', 'jikwonname', 'busername', 'jikwonjik', 'jikwongen', 'jikwonpay'])
    print(df1.head(3))
    print('연봉의 총합 : ', df1['jikwonpay'].sum()  )

    print()
    # csv file i/0

    with open('pandasdb2.csv', mode= 'w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for row in cursor.fetchall():
            writer.writerow(row)

    df2 = pd.read_csv('pandasdb2.csv', header=None, 
                names=['번호', '이름', '부서', '직급', '성별', '연봉'])
    print(df2.head(3))

    print("\n\npandas의 sql 처리 함수 이용 -----------------")
    df = pd.read_sql(sql, conn)
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉']
    print(df.head(2))
    print(df[:2])
    print(df[:-28])
    print(df['이름'].count(), ' ', len(df))
    print('부서별 인원수: ', df['부서'].value_counts())
    print('연봉 7000 이상 : ', df.loc[df['연봉'] >= 7000])
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True)
    print('교차표\n', ctab)

    # 시각화
    jik_ypay = df.groupby(['직급'])['연봉'].mean()     # 직급별 연봉 평균
    print('jik_ypay : ', jik_ypay)

    plt.pie(jik_ypay, explode=(0.2, 0, 0, 0.3, 0),
            labels=jik_ypay.index,
            shadow=True, counterclock=False)
    plt.show()
except Exception as e:
    print('처리 오류 : ', e)
finally:
    cursor.close()
    conn.close()






# pandas 문제 7)
#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
#      - DataFrame의 자료를 파일로 저장
#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
#      - 연봉 상위 20% 직원 출력  : quantile()
#      - SQL로 1차 필터링 후 pandas로 분석 
#             - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    sql = """
        select jikwonno, jikwonname, busername, jikwonpay, jikwonjik
        from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    cursor.execute(sql)

    df = pd.DataFrame(cursor.fetchall(),
                    columns=['사번', '이름','부서명', '연봉', '직급'])
    print(df.head(3))
    print()

#      - DataFrame의 자료를 파일로 저장
    with open('jikwoninfo.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        writer.writerow(df.columns)
        writer.writerows(df.values)

    df2 = pd.read_csv('jikwoninfo.csv')
    print(df2.head(3))
    print()

#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    result = pd.pivot_table(df2, index='부서명', values='연봉', aggfunc=['sum', 'max', 'min'])
    result.columns=['연봉합', '최대', '최소']
    print(result)
    print()

#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    ctab = pd.crosstab(df['부서명'], df['직급'], margins=True)
    print('교차표\n', ctab)
    print()
    
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql = """select jikwonno, jikwonname, gogekno, gogekname, gogektel
        from jikwon left outer join gogek on jikwon.jikwonno=gogek.gogekdamsano
    """
    df3 = pd.read_sql(sql, conn)
    df3 = df3.fillna("담당 고객 X")
    print(df3)
    print()

#      - 연봉 상위 20% 직원 출력  : quantile()
    threshold = df2['연봉'].quantile(0.8)
    print(df2[df2['연봉']>=threshold])
    print()

#      - SQL로 1차 필터링 후 pandas로 분석 
#             - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
    sql = "select jikwonjik as 직급, jikwonpay as 연봉 from jikwon"
    df4 = pd.read_sql(sql, conn)
    pay_median = df4['연봉'].median()
    df4 = df4[df4['연봉'] >= pay_median]
    df4_pivot = df4.pivot_table(values='연봉', index='직급', aggfunc='mean')
    print(df4_pivot)
    print()

#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    buser_ypay = df.groupby(['부서명'])['연봉'].mean()  # 직급별
    print(buser_ypay)
    plt.barh(range(len(buser_ypay)), buser_ypay, alpha=0.4)     # 가로 막대
    plt.yticks(range(len(buser_ypay)), buser_ypay.index)
    plt.xlabel('평균 연봉')
    plt.ylabel('부서별')
    plt.show()

except Exception as e:
    print('처리 오류 : ', e)
    
finally:
    cursor.close()
    conn.close()


#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))

#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력









