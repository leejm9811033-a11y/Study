from abc import *


class AbstractClass(metaclass=ABCMeta):  #추상클래스
    @abstractmethod
    def abcMethod(self):     #추상메소드
        # 추상 메소드는 내용을 안 넣는다.
        # 추상 메소드는 일반 메소드를 가질 수 도 
        # 추상 메소드를 가질 수도 있다.
        # 오버라이딩 필수.
        pass

    def normalMethod(self):  #일반메소드
        print('추상클래스 내의 일반 메소드')

# **************************
#parent = AbstractClass()    #에러:추상클래스는 객체 생성 불가

class Child1(AbstractClass):   #상속

    name = '난 Child1'

    def abcMethod(self):    #선언 강요

        print('추상 메소드를 오버라이드함')
        print("부모가 가진 abcMethod 재정의 : 강요당함")





c1 = Child1()            #생성된 객체의 주소를 치환
print("name", c1.name)

class Child2(AbstractClass):   #상속

    name = '난 Child1'

    def abcMethod(self):    #선언 강요
        print("추상클래스 내의 abcMethod 재정의")

    def normalMethod(self):    # 일반 메소드 재정의 (오버라이딩)
        print("일반 메소드 내 맘대로 내용 변경")     

c2 = Child2()         
c2.abcMethod()
c2.normalMethod()

print("-" * 50)
happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod()




