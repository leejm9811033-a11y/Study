# 메소드 오버라이딩(재정의)
# 부모에서 정의된 메소드를 자식이 동일명의 메소드로 내용만 변경해 사용
# 부모 메소드의 기능을 대체하는 새로운 기능을 가짐

# 사용 목적 : 
# 동작의 구체화(공통 틀은 부모가, 실제 행동은 자식 ****** 중요) 실현
# Polymorphism(다형성) - 같은 메소드이나 객체에 따라 다른 기능을 수행
# 확장, 유지보수에 도움 - 부모 코드는 유지한 채 자식 코드만 변경

# 내가 자식들은 이름은 같지만, 의미는 다른 기능을 사용하라
class Parent:
    def printData(self):
        pass


class Child_1(Parent):
    def abc():
        print("Child_1 고유 메소드")

    def printData(self):
        a = 5 + 6
        # ...
        print("Child_1에서 printData 재정의")      # 메소드 오버라이딩

class Child_2(Parent):
    def printData(self):
        print("Child_1에서 printData override")
        msg = "부모와 동일 메소드명이나 내용은 다르다."
        print(msg)


c1 = Child_1()
c1.printData()
print()
c2 = Child_2()
c2.printData()


print("\n다형성 --")

par = Parent()
par = c1
# print(id(par)) == print(id(c1)) : 둘이 주소는 같음
# print(id(c1))
par.printData()
print()
par = c2
print(id(par))     # 여기서는 서로 주소가 달라짐. 
print(id(c2))
print(id(Child_2))

par.printData()
print("-" * 10)
imsi = c1
imsi.printData()
imsi = c2
imsi.printData()

