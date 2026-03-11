# 상속 


class Person:
    say = "난 사람이야~~~"          # 접근권한 : public
    age = "20"
    __msg = "Good : Private Member"

    def __init__(self, age):
        print("Person 생성자")
        self.age = age

    def printInfo(self):            # 접근권한 : public
        print(f"age : {self.age}, story : {self.say}")

    def helloMethod(self):
        print("안녕")
        print("hello : ", self.say, self.age, self.__msg)       # 이녀석은 Private 멤버 : Person 에서만 유효

print(Person.say, Person.age)
# Person.printInfo()          # TypeError: Person.__init__() missing 1 required positional argument

per = Person("25")
per.printInfo()
per.helloMethod()

print("----" * 20)
class Employee(Person):
    subject = "근로자"          # 항상 local이 우선 # subject, say
    say = "일하는 동물"     # hiding(shadowing)

    def __init__(self):
        print("Employee 생성자")

    def printInfo(self):
        print("Employee Class 의 PrintInfo 호출됨")

    def ePrintInfo(self):
        print(self.subject, self.say, self.age)
        # print(self.__msg)     # 이녀석은 Private 멤버 : Person 에서만 유효
        self.helloMethod()
        self.printInfo()
        print(super().say)      # super()는 부모 메소드든 멤버 필드이든 찾으러 부모 클래스로 감.
        super().printInfo()     # super()로 부모는 가능하지만 조부모는 불가능.
                                # 부모한테 먼저 갔다 가야함.ㄴㄴ

        return self.subject, self.say, self.age # 이건 되네.
emp = Employee()

print(emp.subject, emp.age, emp.say, emp.ePrintInfo()) 
# 여기 emp.ePrintInfo()가 None이 나오네? 수정할 방법은? 
# 그냥 아래로 내려라. ePrintInfo에서 프린트할거 아니면
emp.ePrintInfo()

print("------" * 20)
class Worker(Person):
    def __init__(self, age):
        print("Worker 생성자")
        super().__init__(age)   # 부모 클래스의 생성자 호출

    def wPrintInfo(self):
        print("Worker - wPrintInfo 처리")
        # self.printInfo()        # printInfo() 만 작성하면 모듈로 간다. 그러니 self 넣기
        super().printInfo()

wor = Worker("30")
print(wor.say, wor.age)
wor.wPrintInfo()


print("===" * 10)
class Programmer(Worker):
    def __init__(self, age):
        print("Programmer 생성자")
        # super().__init__(age)     # Bound call
        Worker.__init__(self, age)  # Unbound call


    def pPrintInfo(self):
        print("Programmer - pPrintInfo 처리하였음")


    def wPrintInfo(self):       # 부모 메소드와 동일 메소드 선언
        print("Programmer에서 - overriding")


pro = Programmer("35")
print(pro.say, pro.age)
pro.pPrintInfo()
pro.wPrintInfo()

print("\n클래스 타입 확인")
a = 3; print(type(a))
print(type(pro))            # <class '__main__.Programmer'>
print(type(wor))            # <class '__main__.Worker'>      # 클래스 타입
print(Person.__bases__)     # (<class 'object'>,)            # 오브젝의 멤버, 오브젝은 메이커에서 만듦
                            # 메이커가 만든 오브젝으로 클래스 사용.

print(Employee.__bases__)   # (<class '__main__.Person'>,)
print(Worker.__bases__)     # (<class '__main__.Person'>,)
print(Programmer.__bases__) # (<class '__main__.Worker'>,)











