class Car: # prototype 원형 클래스: Class Car를 원형클래스라고 함.
    
    # 원형클래스는 맴버들을 가지고 있다. : handle, speed, showData(self) 그리고 이들은 public이다.
    # 그래서 누구든 사용가능
    # 멤버 앞에 + 나 - 를 줄수 있다. 이걸로 public과 private을 정할 수 있음.
    # Car 라는 설계도를 만드는 순간, 주소가 생성(만들어짐)
    # 차 설계도는 handle, name과 speed라는 멤버 변수를 가짐.
    # showData라는 메소드도 가짐. 이들은 하나의 객체 공간을 가지게 됨.
    # 이들은 공유 가능한 멤버들 : 공유 자원


    # UML

    handle = 0 # 멤버 필드을 준다. (속성을 준다.)
    speed = 0

    # self의 이 객체의 주소를 기억한다.
    def __init__(self, name, speed):
        self.name = name                # 현재객체의 name에게 지역변수 name(지역변수) 인자값 치환
        self.speed = speed

    def showData(self):     # self는 외부에서 객체주소를 가져온다?
        km = "킬로미터"
        msg = "속도 : " + str(self.speed) + km
        return msg
    

    def printHandle(self):
        return self.handle # class 내에 맴버를부를때는 self를 사용해라.
# 먼저 car1에서 handle이 있나 뒤지고, 없으면 prototype의 handle을 가져온다. ****************************






# Car의 이름을 직접 부름. Car로 찾아감. 그리고 handled의 값을 출력
print(Car.handle)   # 원형(prototype) 클래스의 멤버 호출, 하지만 이렇게는 안 쓴다.

car1 = Car("tom", 10)   # 생성자 호출 후 객체 생성(인스턴스했다)
# car1의 주소는 이 객체의 주소를 기억하고 있다.
print("car1 객체 주소 : ", car1)
# 이 순간 객체가 다시 하나 만들어짐. 그리고 이녀석의 주소는 Car1이 기억함.
# 이 친구이름은 Tom이야. speed는 10이야.
print("car1 : ", car1.name, " ", car1.speed, car1.handle)
# 지금 Car랑 car1 이 따로 있음. 중요.**************
# car1에는 handle이 없다. car1의 객체변수에 handle이 없으니, Car의 handle(원형 클래스의 변수) 에서 가져옴.
# 이것이 공유 멤버.  늘 지역이 우선권을 가짐.


car1.color ="파랑"
print("car1.color : ", car1.color) # color 파랑 맴버라는 것이 추가.
# 이 color는 prototype에 없음.


# 이왕이면 Class는 대문자로 시작하자 약속

# UML(Unified Modeling Language, 통합 모델링 언어)은 소프트웨어 시스템의 구조와 행동을 시각적으로 설계,
# 문서화 및 의사소통하기 위한 표준 그래픽 모델링 언어
# https://seulhee030.tistory.com/56
# sequence diagram, use case diagram, class diagram

car2 = Car("john", 20) 
print("car2 객체 주소 : ", car2)  # 객체 세계에서는 멤버를 확인할 때 "."을 찍어라.
print("car2 : ", car2.name, " ", car2.speed, car2.handle)

print("Car 객체 주소 : ", hex(id(Car)))

# print(Car.color, " ", car2.color)
# type object 'Car' has no attribute 'color'

print(Car, car1, car2)
print(id(Car), hex(id(car1)), id(car2)) # 위에 hex 주소랑 같네. 검증!


print(car1.__dict__) # 속에 있는 맴버를 확인할 수 있음.
print(car2.__dict__)

print("-----------메소드----------------------------")

print("car1 speed : ", car1.showData())
print("car2 speed : ", car2.showData())



car1.speed = 80
car2.speed = 110
print("car1 speed : ", car1.showData())
print("car2 speed : ", car2.showData())

print("car1 handle : ", car1.printHandle())
print("car2 handle : ", car2.printHandle())
# prototype의 printHandle 주석 참조.















