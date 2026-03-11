# oop(객체 지향, 객체 중심 프로그래밍 가능) : 새로운 타입 생성, 포함, 상속, 다형성 등을 구사할 수 있다.
# class(설계도)로 인스턴스 해서 객체를 생성(별도의 이름 공간을 갖음)
# 객체는 멤버필드(변수)와 메소드로 구성
# 자바와 달리 접근 지정자가 없다. 메소드 오버로딩 없다. 오버라이딩만 있다.
# 모듈의 멤버 : 변수, 명령문, 함수, 모듈, 클레스

print("뭔가를 하다가 객체 만들기")

# Boilerplate : 거의 수정하지 않고, 여러곳에서 반복적으로 재사용되는 코드, 텍스트, 문서, 혹은 코드 조각을 의미한다.

def abc(): # 이건 함수
    print("aaa")

class TestClass: # 객체를 만들위한, 혹은 새로운 타입을 만들기 위한 설계도
    aa = 1      # 멤버필드(변수). 현재 클래스 내에서 전역

    def __init__(self): # 특별한 메소드
        print("생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당")

    def __del__(self):     # self는 외부에서 객체주소를 가져온다?
        print("소멸자 : 프로그램 종료시 자동실행. 마무리 작업")

    def printMsg(self):     # 일반 메소드, 메소드라 부른다. 그리고 Argument가 들어가야한다. 여기는 __init__
        name = "한국인"  # 클래스 내에 있는 함수는 메소드다.
        print(name)
    # 생성자, 소멸자, 일반 메소드를 가짐.

print(TestClass) # <class '__main__.TestClass'>,  
# TestClass 타입. 새로운 타입

# Class는 메모리 확보, 그래서 주소가 있음.


test = TestClass() # < ==========================================객체 생성 한 개
# 생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당
# 소멸자 : 프로그램 종료시 자동실행. 마무리 작업

# 콜백 function, 콜백 메소드, 파이썬은 생성자를 하나만 쓸 수 있다.
# 생성자, 소멸자가 여러개면 제일 아래에 있는 친구만 동작하네.
# 클래스의 친구는 객체변수. "."을 찍으면 나옴. 

print("test객체의 멤버 aa : ", test.aa)
# 생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당
# test객체의 멤버 aa :  1
# 소멸자 : 프로그램 종료시 자동실행. 마무리 작업


# Bound Method call, Unbound Method call : class 내에 멤버를 부를 수 있는 2가지 사용법이 있다. 둘 다 알고 있자

# method call 
test.printMsg()     # 1. Bound Method call

""" # self가 들어가야함. 안들어가면 이런 에러
TypeError: TestClass.printMsg() takes 0 positional arguments but 1 was given
    def printMsg():     
        name = "한국인" 
        print(name)
"""

TestClass.printMsg(test)    # 2. Unbound Method call

# TestClass.printMsg()
# TypeError: TestClass.printMsg() missing 1 required positional argument: 'self'


print(type(1))
print(type(1.0))
print(type(test))
print(id(test))     
print(id(TestClass)) # id(test)와 id(TestClass)의 주소가 다르다.


test2 = TestClass() # < ============================================== 객체 생성 한 개 더

print(id(test2))







