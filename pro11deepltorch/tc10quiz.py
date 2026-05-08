# 자전거 공유 시스템 데이터 다중선형회귀분석
# train.csv를 이용하여 대여횟수(count) 예측

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 랜덤 고정
np.random.seed(1)
tf.random.set_seed(1)

# 데이터 읽기
url = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv"
df = pd.read_csv(url)

print(df.head())
print(df.info())

# datetime 처리
df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["day"] = df["datetime"].dt.day
df["hour"] = df["datetime"].dt.hour
df["weekday"] = df["datetime"].dt.weekday

# 변수 선택
# 제외 변수
# datetime : 날짜 문자열이므로 그대로 사용하지 않음
# casual, registered : count를 구성하는 값이므로 예측 변수로 사용하면 데이터 누수 발생
# atemp : temp와 유사한 변수라 제외
feature_cols = [
    "season",
    "holiday",
    "workingday",
    "weather",
    "temp",
    "humidity",
    "windspeed",
    "year",
    "month",
    "day",
    "hour",
    "weekday"
]

target_col = "count"

x_df = df[feature_cols].copy()
y = df[target_col].values.astype("float32")

# 범주형 변수 처리
# season, weather는 숫자로 되어 있지만 범주형 의미가 강하므로 더미 변수로 변환
x_df["season"] = pd.Categorical(x_df["season"], categories=[1, 2, 3, 4])
x_df["weather"] = pd.Categorical(x_df["weather"], categories=[1, 2, 3, 4])

x_df = pd.get_dummies(
    x_df,
    columns=["season", "weather"],
    drop_first=True,
    dtype=int
)

feature_names = x_df.columns.tolist()

print("\n[사용한 최종 변수]")
print(feature_names)

x = x_df.values.astype("float32")

# train / test 분리
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1
)

# 스케일링
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 다중선형회귀 모델
# 은닉층 없이 Dense(1)만 사용하면 선형회귀 모델과 같은 구조
model = Sequential()
model.add(Input(shape=(x_train_scaled.shape[1],)))
model.add(Dense(1, activation="linear"))

model.compile(
    optimizer=Adam(learning_rate=0.01),
    loss="mse",
    metrics=["mae"]
)

# 모델 학습
history = model.fit(
    x_train_scaled,
    y_train,
    epochs=200,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# loss 시각화
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="train loss")
plt.plot(history.history["val_loss"], label="validation loss")
plt.xlabel("Epoch")
plt.ylabel("Loss(MSE)")
plt.title("Training Loss")
plt.legend()
plt.grid(True)
plt.show()

# 예측
y_train_pred = model.predict(x_train_scaled).ravel()
y_test_pred = model.predict(x_test_scaled).ravel()

# 음수 예측값 방지
y_train_pred = np.maximum(y_train_pred, 0)
y_test_pred = np.maximum(y_test_pred, 0)

# 설명력 출력
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
test_mae = mean_absolute_error(y_test, y_test_pred)

print("\n[모델 설명력]")
print(f"Train R² Score : {train_r2:.4f}")
print(f"Test  R² Score : {test_r2:.4f}")
print(f"Test RMSE      : {test_rmse:.2f}")
print(f"Test MAE       : {test_mae:.2f}")

# 표준화된 회귀계수 확인
coef = model.layers[0].get_weights()[0].ravel()
coef_df = pd.DataFrame({
    "feature": feature_names,
    "coef": coef,
    "abs_coef": np.abs(coef)
}).sort_values("abs_coef", ascending=False)

print("\n[대여횟수에 영향을 주는 변수 순위]")
print(coef_df[["feature", "coef"]])

# 새로운 데이터 입력 후 예측
def predict_new_data():
    print("\n[새로운 데이터 입력]")
    print("예시 datetime 입력: 2012-12-20 08:00:00")

    datetime_input = input("datetime 입력 : ")
    dt = pd.to_datetime(datetime_input)

    season = int(input("season 입력(1:봄, 2:여름, 3:가을, 4:겨울) : "))
    holiday = int(input("holiday 입력(0:공휴일 아님, 1:공휴일) : "))
    workingday = int(input("workingday 입력(0:근무일 아님, 1:근무일) : "))
    weather = int(input("weather 입력(1:맑음, 2:흐림/안개, 3:약한 비/눈, 4:폭우/폭설) : "))
    temp = float(input("temp 입력(기온) : "))
    humidity = float(input("humidity 입력(습도) : "))
    windspeed = float(input("windspeed 입력(풍속) : "))

    new_data = pd.DataFrame([{
        "season": season,
        "holiday": holiday,
        "workingday": workingday,
        "weather": weather,
        "temp": temp,
        "humidity": humidity,
        "windspeed": windspeed,
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "hour": dt.hour,
        "weekday": dt.weekday()
    }])

    # 학습 데이터와 동일하게 범주형 처리
    new_data["season"] = pd.Categorical(new_data["season"], categories=[1, 2, 3, 4])
    new_data["weather"] = pd.Categorical(new_data["weather"], categories=[1, 2, 3, 4])

    new_data = pd.get_dummies(
        new_data,
        columns=["season", "weather"],
        drop_first=True,
        dtype=int
    )

    # 학습 때 사용한 컬럼 순서와 동일하게 맞춤
    new_data = new_data.reindex(columns=feature_names, fill_value=0)

    # 스케일링 후 예측
    new_data_scaled = scaler.transform(new_data.values.astype("float32"))
    pred = model.predict(new_data_scaled).ravel()[0]

    # 대여횟수는 음수가 될 수 없으므로 0 미만이면 0 처리
    pred = max(pred, 0)

    print(f"\n예상 자전거 대여횟수 : {pred:.0f}회")

predict_new_data()