# kaggle의 Santander customer satisfacation
# 산탄데르 은행의 고객만족 여부 분류 처리
# 클래스(label)명은 target이고 0:만족, 1:불만족

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split

pd.set_option('display.max_columns', None)

df = pd.read_csv("train_san.csv", encoding='latin-1')
print(df.head(2))
print(df.shape)
print(df.info())

# 전체 데이터에서 만족과 불만족의 비율
print(df['TARGET'].value_counts())
unsatisfied_cnt = df[df['TARGET'] == 1].TARGET.count()
total_cnt = df.TARGET.count()
print(f'불만족 비율은 {unsatisfied_cnt / total_cnt}')

print(df.describe()) # feature의 분포 확인

df['var3'].replace(-999999, 2, inplace=True)
df.drop('ID', axis=1, inplace=True)
print(df.describe())

# feature / label 분리
x_features = df.iloc[:, :-1]
y_label = df.iloc[:, -1]
print('x_features shape : ', x_features.shape)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(
    x_features, y_label, test_size=0.2, random_state=156, stratify=y_label
)
train_cnt = y_train.count()
test_cnt = y_test.count()
print(x_train.shape, x_test.shape)
print('학습데이터 레이블 값 분포 비율', y_train.value_counts() / train_cnt)
print('검증데이터 레이블 값 분포 비율', y_test.value_counts() / test_cnt)

from xgboost.callback import EarlyStopping

xgb_clf = XGBClassifier(n_estimators=100, random_state=12, eval_metric='auc')
xgb_clf.fit(x_train, y_train, eval_set=[(x_test, y_test)], verbose=False)

xgb_roc_score = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:, 1])
print(f'xgb_roc_score : {xgb_roc_score:.5f}')

pred = xgb_clf.predict(x_test)
print('예측값 : ', pred[:5])
print('실제값 : ', y_test[:5].values) 
from sklearn import metrics
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred))

print()
# 최적의 파라미터 구하기
params = {'max_depth':[5, 7], 'min_child_weight':[1, 3], 'colsample_bytree':[0.5, 0.75]}
# max_depth : 트리 깊이, min_child_weight:
gridcv = GridSearchCV(xgb_clf, param_grid=params)
gridcv.fit(x_train, y_train, )
print('gridcv 최적 파라미터 : ', gridcv.best_params_)
xgb_roc_score = roc_auc_score(y_test, gridcv.predict_proba(x_test)[:, -1], average='macro')
# 매크로 평균(Macro-average)과 마이크로 평균(Micro-average)은 
# 다중 클래스 분류(Multi-class Classification) 문제에서 
# 모델의 성능(정밀도, 재현율, F1-score 등)을 평가할 때 
# 사용하는 두 가지 주요 방식입니다.

print(f'xgb_roc_score : {xgb_roc_score:.5f}')
# gridcv 최적 파라미터 : 

print() # 위 파라미터로 모델 생성
xgb_clf2 = XGBClassifier(n_estimators=5, state=12, \
    max_depth=5, min_child_weight=3, colsample_bytree=0.5)

# 중요 피처 시각화
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
plot_importance(xgb_clf2, ax=ax, max_num_features=20)
plt.show()


