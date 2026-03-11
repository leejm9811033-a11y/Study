# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리
# 하나의 파일은 하난의 모듈이 된다.
# 표준 모듈, 사용자 작성 모듈, 제 3자 모듈(third party)로 구분 할 수 있다.

print(print.__module__)     # builtins

print("뭔가를 하다가... 외부 모듈 사용하기")
import sys
#print(sys.path)
# ['C:\\work\\projects\\pro1\\pack1', 
# 'C:\\Users\\acorn\\AppData\\Local\\Python\\pythoncore-3.14-64\\python314.zip', 
# 'C:\\Users\\acorn\\AppData\\Local\\Python\\pythoncore-3.14-64\\DLLs', 
# 'C:\\Users\\acorn\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib', 
# 'C:\\Users\\acorn\\AppData\\Local\\Python\\pythoncore-3.14-64', 
# 'C:\\Users\\acorn\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages']

a = 5
if a > 7:
    sys.exit() # 응용 프로그램 강제 종료

print("end") # sys.exit() 때문에, 여기는 안 나옴
print(sys.path) # sys.exit() 때문에, 여기는 안 나옴


import math
print(math.pi) # math에 "."을 찍으로 함수가 쫙나옴.
# 3.141592653589793

import calendar

calendar.setfirstweekday(6)
calendar.prmonth(2026,1)
del calendar

import random
# 대문자로 사용하면, 변수를 안 바꾼다. 보이지 않는 약속.
print(random.random())
print(random.randrange(1, 10))

# random.random , random.randrange 으로 코딩하면 힘드니, from을 사용.
from random import random, randrange # 묘듈의 멤버
from random import * # 별로 추천을 안 함. 메모리 관리
print(random())
print(randrange(1, 10))

#print(random.randrange(1, 10))
# AttributeError: 'builtin_function_or_method' object has no attribute 'randrange'


print("end")



