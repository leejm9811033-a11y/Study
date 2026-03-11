kor = 100   # 모듈의 전역변수

def abc():
    eng = 0     # 함수 내의 지역변수
    print("모듈의 멤버 함수")

class My:
    kor = 80    # My 멤버 변수 (필드)

    def abc(self):
        print("My 멤버 메소드")

    def show(self):
        # kor = 77      # 메소드 내의 지역 변수
        print(kor)      # 모듈의 전역변수에서 가져옴 # 100
        print(self.kor) # Class를 붙이면, My 멤버 변수를 가져옴. # 80
        self.abc()      # My 멤버 메소드
        abc()           # 모듈의 멤버 함수

my = My()
my.show()

print("-------------------------")
print(My.kor)           # 80 : My 멤버 변수 (필드)
tom = My()
print(tom.kor)          # 80 : tom 멤버 변수 (필드)

tom.kor = 88
print(tom.kor)          # 80 : tom 멤버 변수 (필드)


oscar = My()
print(oscar.kor)








