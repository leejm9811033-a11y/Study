# 상속 : 자원의 재활을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
# 코드 재사용
# 확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공통개념은 부모 클래스, 구체적 내용은 자식 클래스에서 구현한다.
# 다형성 구사 - 메소드 오버라이딩

# 포함과 상속은 다르다.
# 클래스에는 "강 결합 - 상속", "약 결합 - 포함" 이 있다.
# 프로그램을 만들면 유지보수가 불편해진다. (너무 강하게 연결되어 있어서. 변경 추가 수정 삭제가 힘들다.)
# 하지만 다형성은 "상속"에서만 가능하다. (그래서 다형성 사용하려면 상속을 사용)

# 다중 상속이 가능하지만, 다이아몬드? 상속을 조심해야함.

class Animal: # 동물들이 가져야할 공통 속성과 행위 선언
    age = 1

    def __init__(self):
        print("Animal 생성자")

    def move(self):
        print("움직이는 생물이다.")


class Dog(Animal):              # 상속 - Animal : 부모, 조상, super, parent  # 이것이 상속이다.
                                # Dog : 자식, 자손, 파생, sub, child 클래스
    def __init__(self):
        print("Dog 생성자")

    def my(self):
        print("댕댕이라고 해요")


dog1 = Dog()
dog1.my()
dog1.move() # 일단 Dog에서 찾아보고, 없으면 부모클래스 Animal로 간다.
print("age : ", dog1.age)
print()
dog2 = Dog()
dog2.my()
dog2.move()

print()

class Horse(Animal):

    pass

horse1 = Horse()
horse1.move()








# 클래스에는 "강 결합 - 상속", "약 결합 - 포함" 이 있다.