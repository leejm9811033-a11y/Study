# 편차가 큰 데이터에 대한 로그 변환

# ML에서 데이터 분석 시 log를 사용하면?

# 1) 스케일을 줄여서 다루기 쉽다.
# 스케일 차이를 축소해 준다. log(10)=1, log(10**x)=x
# 2) 로그변환하며 치우친 데이터를 정규분포에 가깝게 변경 가능
# 3) 모델링에서 지수 관계를 선형 관계로 바꿔준다.   y = a * x⁹

import numpy as np

np.set_printoptions  # 3.45e+02 이런 과학적 표기 바꿈
def test():
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    print(np.log2(3.45), ' ', np.log10(3.45), ' ', np.log(3.45))

    print("원본 값 : ", values)
    log_values = np.log10(values)
    print('log_values : ', log_values)  # 상용로그
    ln_values = np.log(values)
    print('ln_values : ', ln_values)   # 자연로그

    # 정규화 : 모든 데이터를 0 ~ 1사이의 범위 내에서 표시
    min_log = np.min(log_values)
    max_log = np.max(log_values)
    normalized = (log_values - min_log) / (max_log - min_log)

    print("정규화 결과 : ", normalized)


class LogTrans:
    # 편차가 큰 데이터를 로그 스케일 변환하고 그 역변환을 클래스로 제공
    def __init__(self, offset:float=1.0):
        self.offset = offset

    # 로그 변환 메서드  
    def transform(self, x: np.ndarray) -> np.ndarray:
        return np.log(x + self.offset)

    # 역 변환 메소드
    def  inverse_trans(self, x_log:np.ndarray) -> np.ndarray:
        return np.exp(x_log)




def main():
    test()
    print('***' * 10)
    data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype=float)

    log_trans = LogTrans(offset=1.0)

    data_log_scaled = log_trans.transform(data)                 # 로그 변환
    reversed_data = log_trans.inverse_trans(data_log_scaled)    # 역변환

    print("원본 : ", data)
    print("로그변환 : ", data_log_scaled)
    print("역변환 : ", reversed_data)

if __name__ == "__main__":
    main()
