# 단순선형회귀 : ols의 Regression Results의 이해
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(df.head(3))
print(df.corr())

model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
print(model.summary())
print('parameters : ', model.params)# 회귀계수를 봐야함.
print('R-squared : ', model.rsquared)
print('p-value : ', model.pvalues)      # print('predict values : ', model.predict())
print('예측값 : ', model.predict()[:5])
print('실제값 : ', df.만족도[:5].values)

plt.scatter(df.적절성, df.만족도)
slope, intertcept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, slope * df.적절성 + intertcept, c='b')
plt.show()

# t-value = 기울기 / 표준 오차


# 기울기, 표준 오차, p-value 관계

# 독립변수가 종속변수의 영향력이 클 수록 좋다. 이때, 벤다이어그램에서 겹치는 부분이 결정 계수

# https://aliencoder.tistory.com/40     # 여기 그림 꼭 확인하기 FIG 1.

# sse ssr sst


