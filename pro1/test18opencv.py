# Computer Vision(opencv:Open Source Computer Vision 라이브러리 사용

# pip install opencv-python

import cv2
print(cv2.__version__)  # 5.0.0

img1 = cv2.imread("test18ani.jpeg")
print(type(img1))  # <class 'numpy.ndarray'>

cv2.imshow("img test", img1)
cv2.waitKey()
cv2.destroyAllWindows()
# print("end")

# 다른 이름으로 저장
cv2.imwrite("test18ani2.jpg", img1)
cv2.imwrite("test18ani3.jpg", img1, [cv2.IMWRITE_JPEG_QUALITY, 10])  # 이미지 품질을 떨어트림

# 이미지 크기 조정
img2 = cv2.resize(img1, (300,300), interpolation=cv2.INTER_AREA)
cv2.imwrite("test18ani4.jpg", img2)

# 밝기, 상하좌우 회전, 자르기 ... 등등 모두 지원


