# 단순선형회귀 - iris dataset
# 상관관계가 약한 경우와 강한 경우로 분석모델을 생성 후 비교

import pandas as pd 
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head(3), type(iris))
print(iris.iloc[:, 0:4].corr())

print("\n연습 : 상관관계가 약한 변수를 사용  -0.117570")
result1 = smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
print(result1.summary())
print('R squared : ', result1.rsquared)     # 0.013822654   # 이정도의 설명률(R squared)은 무시
print('p-value : ', result1.pvalues.iloc[1])    # 0.1518982607 > 0.05   이 모델은 유의하지 않다.
# 시각화
plt.scatter(iris.sepal_width, iris.sepal_length)
plt.plot(iris.sepal_width, result1.predict(), color='r')
plt.show()

print("\n연습2 : 상관관계가 강한 변수를 사용  0.871754")
result2 = smf.ols(formula='sepal_length ~ petal_length', data=iris).fit()
print(result2.summary())
print('R squared : ', result2.rsquared)     # 0.759954645   # 이정도의 설명률(R squared)은 의미 있음
print('p-value : ', result2.pvalues.iloc[1])    # 1.0386674 < 0.05   이 모델은 유의하다.
# 시각화
plt.scatter(iris.petal_length, iris.sepal_length)
plt.plot(iris.petal_length, result2.predict(), color='b')
plt.show()


print('실제값 : ', iris.sepal_length[:10].values)
# [5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9]
print('예측값 : ', result2.predict()[:10])
# [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946  5.00177129 4.8790946  4.91998683 4.8790946  4.91998683]

# 모델을 만들때, 오버피팅(과적합)과 언더피팅을 조심하자. 어느정도만 맞으면 된다.

print()
# 새로운 값으로 예측 
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 6.0]})
y_pred = result2.predict(new_data)
print('예측결과 : ', y_pred.values)     # 예측결과 :  [4.75641792 4.51106455 6.76013708]

print("\n연습2 : 독립변수를 복수로 사용 - 다중선형회귀")
# result3 = smf.ols(formula='sepal_length ~ petal_length + petal_width', data=iris)
column_select = "+".join(iris.columns.difference(['sepal_length','sepal_width','species']))
print(column_select)
result3 = smf.ols(formula='sepal_length ~ ' + column_select, data=iris).fit()
print(result3.summary())


