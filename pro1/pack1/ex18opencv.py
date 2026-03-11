# opencv(Computer Vision)
# 영상처리, 패턴인식, 색상처리, 주파수 변화
# conda install opencv-python 은 안 되네.
# pip install opencv-python  으로 처리(터미널) 
# C:\work\projects\pro1\pack1
# ani.jpeg

import cv2

print(cv2.__version__)      # 4.13.0
img1 = cv2.imread("ani.jpeg")
print(type(img1))           # <class 'numpy.ndarray'>

cv2.imshow("image test", img1)
cv2.waitKey()               # 이 줄이 있어야. 이미지 유지, 무한루프에 빠짐
cv2.destroyAllWindows()     # 이미지 유지 종료


cv2.imwrite("ani2.jpeg", img1)
cv2.imwrite("ani2.jpeg", img1, [cv2.IMWRITE_JPEG_QUALITY,10])

# dir *.j* (터미널), dir ani*    (이미 복사)


# 이미지 크기 조절
img2 = cv2.resize(img1, (300, 100), interpolation=cv2.INTER_AREA)
cv2.imwrite("ani2.jpg", img2)

# 이미지 밝기 조정
# 이미지 상하좌우 회전
# 특정 영역 자르기
# ...








print("end")





