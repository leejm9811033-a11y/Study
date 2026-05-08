# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# import seaborn as sns

# iris = sns.load_dataset('iris')
# print(iris)
# X_iris = iris.drop('species', axis=1)
# y_iris = iris['species']

# X_train, X_test, y_train, y_test = train_test_split(X_iris,y_iris, random_state = 1)
# print(len(X_train))
# print(len(X_test))

# from sklearn.naive_bayes import GaussianNB
# model = GaussianNB()
# model.fit(X_train, y_train)
# pred = model.predict(X_test)
# print(pred)

# from sklearn.metrics import accuracy_score
# print('accuracy_score : ', accuracy_score(y_test, pred))

# from sklearn.decomposition import PCA

# model = PCA(n_components=2)

# model.fit(X_iris)  # 독립변수만 입력, Label(y)는 지정하지 않음

# result = model.fit_transform(X_iris)  # 데이터를 2차원으로 변환


# print(result)
# # [[-2.68412563  0.31939725]
# #  [-2.71414169 -0.17700123]
# #  [-2.88899057 -0.14494943] ...

# iris['PCA1'] = result[:, 0]
# iris['PCA2'] = result[:, 1]
# sns.lmplot('PCA1', 'PCA2', data=iris, hue='species', fit_reg = False)
# plt.show()
# # PCA 모델이 iris의 Label에 대한 지식이 없는데도 2차원 표현에서 종류가 2개로 잘 분류된 것을 알 수 있다. 




# import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits

# digits = load_digits()
# print(digits.DESCR)
# data = digits.data
# label = digits.target
# print(data.shape, label.shape) # (1797, 64) (1797,)
# print(data[0].shape)  # (64,)  64 차원 짜리 데이터

# plt.imshow(data[0].reshape((8, 8)))
# plt.show()
# print(label[0])

# from sklearn.decomposition import PCA
# pca = PCA(n_components=2) # 2차원으로 차원 축소

# print(pca.fit(data)) # 데이터에서 특징 찾기(주성분 찾기)
# # PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
# #     svd_solver='auto', tol=0.0, whiten=False)
# new_data = pca.fit_transform(data)  # projection(사영)하기

# print('원본 데이터의 차원 : ', data.shape)
# print('PCA를 거친 데이터의 차원 : ', new_data.shape)
# print(new_data[:2])  # [[ -1.25946787  21.27488269] [  7.95760631 -20.76870689]]

# plt.scatter(new_data[:, 0], new_data[:, 1], c= label, linewidths=1, edgecolors='black')
# plt.show()



# from sklearn.cluster import KMeans
# kmodel = KMeans(n_clusters=3, init='random', random_state=0) #'k-means++'
# # n_clusters:클러스터 개수 지정
# # init: 초기 클러스터 중심을 선택하는 방법 지정(초기값은 k-means++)

# x = kmodel.fit_predict(X_train)  # k-means 클러스터링으로 구분한 결과 얻기
# print('pred : ', x) 


# # 위 두개의 그래프 결과 두 변수는 공통적인 특징이 있으므로 차원 축소의 근거가 있다고 판단.
# # PCA를 진행
# # 순서1 : 입력 데이터의 공분산 행렬을 생성한다.
# # 순서2 : 공분산 행렬의 고유벡터와 고윳값(고유벡터 크기)을 계산한다.
# # 순서3 : 고윳값이 큰 순서대로 k개(PCA 변환 차수 만큼) 만큼 고유벡터 추출
# # 순서4 : 고윳값이 가장 큰 순으로 추출된 고유벡터를 이용해 새롭게 입력 데이터를 변환한다.
# # sklearn의 PCA를 이용하면 순서대로 진행을 함.



# pca1 = PCA(n_components=1)  # 변환할 차원수
# x_low = pca1.fit_transform(x) # 특징행렬을 낮은 차원의 근사 행렬로 변환

# print('x_low : ', x_low, ' ', x_low.shape)

# # 주성분 값 원복하기
# x2 = pca.inverse_transform(x_low)
# print('원복 후 x2: ', x2, ' ', x2.shape)
# print('원본 : ', x[0, :])
# print('주성분 : ', x_low[0])
# print('원복 : ', x2[0, :])

# # 주성분 분석값을 기반으로 시각화
# # pca 방향벡터
# pc1 = pca1.components_[0]
# mean = x.mean(axis=0)

# df = pd.Dataframe(x)
# ax = sns.scatterplot(x=0, y=1, data=df, marker='s', s=100, color='b')
# # 각 점에 대해 text 표시
# for i in range(n):
#     ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, f'표본{i + 1}')

# # PCA 축 (화살표)
# plt.quiver(
#     mean[0], mean[1], # 시작점(평균)
#     pc1[0], pc1[1]
#     scale=3, color='r', width=0.01
# )
# plt.xlabel('꽃받침길이')
# plt.ylabel('꽃받침폭')
# plt.title('아이리스 특성 + 제1주성분')
# plt.axis('equal')
# plt.grid(True)
# plt.show()

# print('***' * 10)
# # 원본 열 4개를 차원축소해 2개의 열로 변환 후 SVM 부류 모델을 
# x = iris.data
# print(x[0, :])
# pca2 = PCA(n_components=2)
# x_low2 = pca2.fit_transform(x)
# print('x_low2 : ', x_low2[0, :], ' ', x_low2.shape)
# # 변동성 비율
# print(pca2.explained_variance_ratio_)
# x4 = pca2.inverse_transform(x_low2)
# print('최초자료 : ', x[0])
# print('차원축소 : ', x_low2[0])
# print('차원복귀 : ', x4[0, :])
# print()
# iris1 = pd.DataFrame(x, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
# print(iris1.head(3))
# iris1 = pd.DataFrame(x_low2, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
# print(iris2.head(3))

# from sklearn import svm, metrics
# feature1 = iris1.values
# print(feature1[:3])
# label = iris.target
# print(label[:3])

# print('원복 데이터로 SVM')
# model1 = svm.SVC(C=0.1, random_state=0).fit(feature1, label)
# pred1 = model1.predict(feature1)
# print('model1 accuracy : ', metrics.accuracy_score(label, pred1))

# print('PCA 데이터로 SVM 분류 모델 작성')
# feature2 = iris2.values
# print(feature2[:3])
# print(label[:3])

# model2 = svm.SVC(C=0.1, random_state=0).fit(feature2, label)
# pred2 = model2.predict(feature2)
# print('model2 accuracy : ', metrics.accuracy_score(label, pred2))




