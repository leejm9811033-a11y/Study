# 다중선형회귀 : 자동차 연비 예측
# 조기종료 코드 추가

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datas = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/auto-mpg.csv")
print(datas.head(2))
print(datas.info())
del datas['car name']

datas['horsepower'] = pd.to_numeric(datas['horsepower'], errors='coerce')
datas = datas.dropna()
print(datas.isna().sum())

datas.drop(['cylinders','acceleration','model year','origin'],    \
    axis='columns', inplace=True)
print(datas.head(2))

# sns.pairplot(datas[['mpg', 'displacement', 'horsepower', 'weight']],
#             diag_kind='kde')
# plt.show()

# train / test split
train_dataset = datas.sample(frac=0.7, random_state=123)
print(train_dataset[:2], train_dataset.shape)   # (274, 4)
test_dataset = datas.drop(train_dataset.index)
print(test_dataset[:2], test_dataset.shape) # (118, 4)

# 표준화 : (요소값 - 평균) / 표준편차
train_stat = train_dataset.describe()
train_stat.pop('mpg')
print(train_stat)
train_stat = train_stat.transpose() # 전치
print(train_stat)

def stdscale_func(x):
    return  (x - train_stat['mean']) / train_stat['std']

train_label = train_dataset.pop('mpg')
print(train_label[:3])
test_label = test_dataset.pop('mpg')
print(test_label[:3])

# print(stdscale_func(train_dataset[:3]))
st_train_data = stdscale_func(train_dataset)
print(st_train_data[:3])

st_test_data = stdscale_func(test_dataset)
print(st_test_data[:3])

# model
def build_model():
    network = Sequential([
        Input(shape=(3, )),
        Dense(units=32, activation='relu'),
        Dense(units=16, activation='relu'),
        Dense(units=1, activation='linear')
    ])
    opti = tf.keras.optimizers.Adam(learning_rate=0.01)

    network.compile(optimizer=opti, loss='mean_squared_error',
                    metrics=['mean_squared_error','mean_absolute_error'])
    return network

model = build_model()
print(model.summary())

EPOCHS = 5000

# 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',  # 뭘 기준으로 정할지를 결정.   loss, val_loss
    patience=5,  # 몇번의 epoch까지 더 기다릴지 결정
    restore_best_weights=True   # 학습 중 가장 성능이 좋은 epoch의 가중치를 취함
    # baseline=0.01 # 최소한의 성능
)

history = model.fit(x=st_train_data, y=train_label, batch_size=32, \
                    epochs=EPOCHS, verbose=2,
                    validation_split=0.2,
                    callbacks = [early_stop]
)

df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)

# 모델 학습 정보 시각화
def plt_history(df):
    hist = df
    hist['epoch'] = history.epoch
    # print(hist.head())

    plt.figure(figsize=(8, 14))
    plt.subplot(2, 1, 1)
    plt.xlabel('epoch')
    plt.xlabel('mae [mpg]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='train err')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='validation err')
    plt.legend()
    plt.subplot(2, 1, 1)
    plt.xlabel('epoch')
    plt.xlabel('mae [mpg]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='train err')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='validation err')
    plt.legend()
    plt.show()

plt_history(df)

# 모델 평가
from sklearn.metrics import r2_score
loss, mse, mae = model.evaluate(st_test_data, test_label)
print(f'loss {loss:.3f}')
print(f'mse {mse:.3f}')
print(f'mae {mae:.3f}')
print('결정 계수 : ', r2_score(test_label, model.predict(st_test_)))

# 새로운 값으로 예측
new_data = pd.DataFrame({
    'displacement':[300,400],   # 선형회귀의 충족 조건 5가지
    'horsepower':[120, 150],
    'weight':[2000, 4000]
})
new_st_data = stdscale_func(new_data)
new_data_pred = model.predict(new_st_data).ravel()
print('새 값 예측결과 : ', new_data_pred)



