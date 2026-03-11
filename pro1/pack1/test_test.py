class ElecProduct:
    volum = 0

    def volumeControl(self, volume):
        print(f"볼륨을 조절한다. : {volume}")
        pass

class ElecTv(ElecProduct):
    def tv_1(self):
        print("ElecTv 고유 메소드")

    def volumeControl(self, volume):
        # 계산 ...
        print("금요일 와우")
        self.volum = volume # 있어도 없어도 같음
        print(f"ElecRadio 고유 메소드 : {volume}")

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        sound = volume
        print(f"ElecRadio 고유 메소드 : {sound}")

    pass

product = ElecProduct()
tv = ElecTv()
product = tv
product.volumeControl(5)
print()                     # product() 라고하면, TypeError: 'ElecTv' object is not callable
radio = ElecRadio()
product = radio
product.volumeControl(3)

print("---------------------")
q1 = [ElecTv(), ElecRadio()]
for a in q1:
    a.volumeControl(2)
    print()

#--------------------------------------



class Animal:

    def move(self):
        print("대부분의 동물들은 4발로 걸어요.")



class Dog(Animal):
    name = "개"

    def move(self):
        print("댕댕이")


class Cat(Animal):
    name = "고양이"

    def move(self):
        print("냥냥이")


class Wolf(Dog, Cat):
    pass


class Fox(Cat, Dog):
                    # self를 안 넣으면/ 아래 에러
    def move(self):     # TypeError: Fox.move() takes 0 positional arguments but 1 was given
        print("여우")
        pass

    def foxMethod(self):
        print("Fox 고유 메소드")
        pass        # 자식이 없는데 pass를 쓰면 이상하다.
                    # 끝에 있는 클래스를 터미널이라고 하나?

animal = [Dog(), Cat(), Wolf(), Fox()]


for a in animal:
    print("-" * 100)
    print(id(a))
    a.move()









for _ in range(T):

    S, P = map(int, input().split())

    # X^2 + S*X + P

    D = S*S - 4*P


    if D < 0:
        print("No")
        continue

    r = int((D) ** 0.5)

    if r*r != D:
        print("No")
        continue

    J = S + r

    if (J % 2) != 0:
        print("No")
        continue

    N = J // 2

    M = S - N

    if N >= 1 and M >= 1 and (N * M) == P:
        print("Yes")
    else:
        print("No")

    



























"""

# S(sum), P(곱)
import math

out = []
for _ in range(T):

    S, P = map(int, input().split())

    D = S*S - 4*P

    if D < 0:
        out.append("No")
        continue        # continue하면 다음 반복문으로 가나?

        continue
        # 를 만나면 현재 for 반복의 나머지 코드는 건너뛰고, 바로 다음 _ 반복으로 넘어가.
        
        


    r = math.isqrt(D)     # isqurt는 integer square root
    if r*r != D:          # 여기는 어떤 상황이지?
        out.append("No")  # r = math.isqrt(D) 이걸 구했는데 검토하는건가?
        continue

    if (S + r) % 2 != 0:
        out.append("No")
        continue

    N = (S + r) // 2
    M = S - N

    if N >= 1 and M >= 1 and N * M == P:
        out.append("Yes")
    else:
        out.append("No")


"""




