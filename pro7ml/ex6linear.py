# # 전통적 방법의 선형회귀(기계학습 중 지도학습)
print('방법4 : make_Regression 사용. model 생성 X')

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# IQ에 따른 시험 점수 예측
score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/score_iq.csv")
print(score_iq.head(3))
print(score_iq.info())
x = score_iq.iq
y = score_iq.score
print(x[:3])
print(y[:3])

# print('상관 계수 : ', np.corrcoef(x, y)[0, 1])  # 0.88222
# print(score_iq[['iq','score']].corr())

# plt.scatter(x, y)
# plt.show()

# # 단순 선형회귀 분석    (인과관계가 있다는 가정하에 진행)
# model = stats.linregress(x, y)
# print(model)    # LinregressResult(slope=np.float64(0.6514309527270075), intercept=np.float64(-2.8564471221974657), rvalue=np.float64(0.8822203446134699), pvalue=np.float64(2.8476895206683644e-50), stderr=np.float64(0.028577934409305443), intercept_stderr=np.float64(3.546211918048538))
# print('기울기 : ', model.slope)
# print('절편 : ', model.intercept)
# print('p값 : ', model.pvalue)

# plt.scatter(x, y)
# plt.plot(x, model.slope * x + model.intercept, c='r')
# plt.show()
# # predict() 메소드를 지원하지 않음
# # print('점수예측 : ', np.polyval([model.slope, model.intercept],
# #                     np.array(score_iq['iq'])))

# newdf = pd.DataFrame({'iq':[55,66,77,88,150]})
# print('점수예측 : \n', np.polyval([model.slope, model.intercept], newdf))

#----------------------------------------------------------------

# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.  

score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv")
print(score_iq.head(3))
print(score_iq.info())
x = score_iq.iq
y = score_iq.score
print(x[:3])
print(y[:3])



model = stats.linregress(x, y)
print(model)    # LinregressResult(slope=np.float64(0.6514309527270075), intercept=np.float64(-2.8564471221974657), rvalue=np.float64(0.8822203446134699), pvalue=np.float64(2.8476895206683644e-50), stderr=np.float64(0.028577934409305443), intercept_stderr=np.float64(3.546211918048538))
print('기울기 : ', model.slope)
print('절편 : ', model.intercept)
print('p값 : ', model.pvalue)




"""
구분,지상파,종편,운동

1,0.9,0.7,4.2

2,1.2,1.0,3.8

3,1.2,1.3,3.5

4,1.9,2.0,4.0

5,3.3,3.9,2.5

6,4.1,3.9,2.0

7,5.8,4.1,1.3

8,2.8,2.1,2.4

9,3.8,3.1,1.3

10,4.8,3.1,35.0

11,NaN,3.5,4.0

12,0.9,0.7,4.2

13,3.0,2.0,1.8

14,2.2,1.5,3.5

15,2.0,2.0,3.5
"""
