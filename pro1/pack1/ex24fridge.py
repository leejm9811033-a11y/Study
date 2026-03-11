# 클래스의 포함관계 연습
# 포함과 상속은 다르다.

class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print("냉장고 문을 열기")

    def close(self):
        self.isClose = False
        print("냉장고 문을 닫기")

    def FoodsList(self):    # 냉장고 문이 열린 경우 음식물 확인
        for f in self.foods:
            print(f" - {f.name} {f.expiry_data}")
        print()

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고에 {thing.name} 넣음") # thing.name => thing으로 하면?! print가 실행이 안되네. 이유는?
            self.FoodsList()
        else:
            print("냉장고 문이 닫혀있음")

class FoodData:
    def __init__(self, name, expiry_data):
        self.name = name
        self.expiry_data = expiry_data


reFrigerator = Fridge()

apple = FoodData("사과", "2026-8-1")

# reFrigerator.put(apple)
reFrigerator.open()
reFrigerator.put(apple)
reFrigerator.close()
print()
cola = FoodData("콜라", "2027-11-1")

reFrigerator.open()
reFrigerator.put(cola)
reFrigerator.close()





