from abc import *

class Employee(metaclass=ABCMeta):  # 추상클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def data_print(self):   #추상메소드
        pass

    def irumnai_print(self):                # 이름, 나이 출력용
        print("이름 : " + self.name + ", 나이 : " + str(self.age) + ",", end = " ")


class Temporary(Employee):
    def __init__(self, name, age, ilsu, ildang):
        # self.name = name
        # self.age = age

        Employee.__init__(self, name, age) # 여기 뒤에 : 붙이면 이상해짐.
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        return self.ilsu * self.ildang


    def data_print(self):   #추상메소드
        print("Temporary")
        # self.irumnai_print()                  # 두 가지 방법이 있다.
        super().irumnai_print()
        print(f"월급 : {int(self.pay())}")
    


class Regular(Employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def pay(self):
        pass

    def data_print(self):
        print("Regular")
        self.irumnai_print()
        print(f"급여 : {int(self.salary)}")


class Salesman(Regular):

    def __init__(self, name, age, salary, sales, commission):
        self.name = name
        self.age = age
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def pay(self):
        pass

    def data_print(self):
        print("Salesman")
        self.irumnai_print()
        print(f"수령액 : {int(self.salary + self.sales * self.commission)}")


t = Temporary("홍길동", 25, 20, 15000)
r = Regular("한국인", 27, 3500000)
s = Salesman("손오공", 29, 1200000, 5000000, 0.25)


print(s.pay())


t.data_print()
r.data_print()
s.data_print()

