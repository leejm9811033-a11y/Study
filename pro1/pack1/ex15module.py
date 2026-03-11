# pack/ex15module - main
print("사용자 정의 모듈 처리하기")

s = 10  # 뭔가를 하다가...

print("\n경로 지정 방법1 : import 모듈명")

import pack1.mymod1
# import 안하면, NameError: name 'mymod1' is not defined

print(dir(pack1.mymod1))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'kbs', 'listHap', 'mbc', 'tot']

"""
tot = 100 # 전역변수

def listHap(*ar):
    print(ar)

def kbs():
    print("대한민국 대표방송")

def mbc():
    print("문화방송")
"""
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__) # C:\work\projects\pro1\pack1\mymod1.py
print(pack1.mymod1.__name__) # mymod1

list1 = [1, 2]
list2 = [3, 4, 5]

pack1.mymod1.listHap(list1, list2) # ([1, 2], [3, 4, 5])

""" # mymod1 안에 있는 함수
def listHap(*ar):
    print(ar)
    if __name__ == "__main__": # 
        print("나는 메인 모듈!!!") # ex15module1가 __name__ 그리고 "__main__"
# mymod1는 메인 모듈이 아니라 안 찍힘.
"""


# if __name__ == "__main__": print("와우 메인 모듈~~~")
# 와우 메인 모듈~~~     # 여기는 메인이라 출력




print("\n경로 지정 방법2 : from 모듈명 import 함수명(메소드명) 또는 변수, ...")

from pack1.mymod1 import kbs
kbs()
from pack1.mymod1 import mbc, tot
mbc()
""" 이렇게 출력
대한민국 대표방송
문화방송
"""
print(tot)



from pack1.mymod1 import * # *을 사용해 mymod1 모듈의 모든 메머 로딩(비권장)
print("tot : ", tot)

from pack1.mymod1 import mbc as 엠비씨만세별명
mbc()
엠비씨만세별명()
"""
문화방송
문화방송
"""

print("\n경로 지정 방법3 : import 하위패키지.모듈명")
import pack1.subpack.sbs
pack1.subpack.sbs.sbsMansae()

import pack1.subpack.sbs as nickname
nickname.sbsMansae()

""" # module도 꼭 저장하기.
def sbsMansae():
    print("에스비에스 만세!")
"""
print("\n경로 지정 방법4 : 현재 package와 동등한 다른 패키지 모듈 읽기")

# PRO1 폴더로 갔다가 pack1_other 폴더로 가야함.
# import ../pack1_other.mymod2

from pack1_other import mymod2
mymod2.hapFunc(7, 8)

print(mymod2.hapFunc(7, 8))
# ModuleNotFoundError: No module named 'pack1_other'
# 터미널 명령어 : cd ..

# 모든 파일에 저장은 꼭 하세요.
# 터미널 명령어 : (myproject) C:\work\projects\pro1>   python -m pack1.ex15module

# 터미널 명령어 : (myproject) C:\work\projects\pro1>   python -m pack1.ex15module.py
# C:\Users\acorn\anaconda3\envs\myproject\python.exe: Error while finding module specification for 'pack1.ex15module.py' (ModuleNotFoundError: __path__ attribute not found on 'pack1.ex15module' while trying to find 'pack1.ex15module.py'). Try using 'pack1.ex15module' instead of 'pack1.ex15module.py' as the module name.


# C:\Users\acorn\anaconda3\envs\myproject\Lib : 여기서 가져온 import mymod3
import mymod3
result = mymod3.gopFunc(4, 3)

print("path가 설정된 곳의 module 읽기 - result:", result)
# print(mymod3)
# # <module 'mymod3' from 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib\\mymod3.py'>

# import sys
# print(sys) 
# # <module 'sys' (built-in)>


# https://docs.python.org/
# Library reference
# 오른쪽 위 검색에 turtle 
# turtle — Turtle graphics



# 내 PC의 속성 => 고급 시스템 설정 => 시스템 속성 => 환경 변수에
# acorn에 대한 사용자 변수와 시스템 변수에 path 경로가 있음



print("end")






