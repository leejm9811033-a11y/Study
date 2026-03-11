# 클래스의 다중 상속 - 부모가 복수
# 다중 상속 : 부모가 두 군데 이상인데, 상속받음.

# cry를 핵심적으로 보자구나. cry는 둘다 받을 순 없다.

class Tiger:
    data = "호랑이 세계"

    def cry(self):
        print("호랑이 : 어흥")

    def eat(self):
        print("맹수는 고기를 좋아함")

class Lion:
    def cry(self):
        print("사자 : 으르렁")

    def hobby(self):
        print("백수의왕은 낮잠이다.")

class Liger_1(Tiger, Lion): # 다중 상속은 순서가 중요
    pass

a1 = Liger_1()
print(a1.data)
a1.eat()
a1.hobby()
a1.cry() # class Liger_1(Tiger, Lion): 
# 호랑이 : 어흥
# 먼저 작성된 Tiger의 cry가 나옴.

print("--" * 10)

# 여기는 hobby가 사방에 있음.

def hobby():
    print("모듈의 멤버 : 일반 함수")

class Liger_2(Lion, Tiger):
    data = "라이거 만세"

    def play(self):
        print("라이거 고유 메소드")

    def hobby(self):
        print("라이거는 공원 걷기를 좋아함")



    def showData(self):
        self.hobby()
        super().hobby()         # super에서 () 붙이기.
        hobby()

        self.eat()
        super().eat()
        print(self.data + " " + super().data)


a2 = Liger_2()
a2.cry()
a2.showData()
