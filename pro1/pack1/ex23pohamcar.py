# 여러 개의 부품 객체를 조립해서 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용)
# 다른 클래스를 마치 자신의 멤버처럼 선언하고 사용.

# (클래스, 객체, 인스턴스) 3개는 뉘양스가 다르다.

from ex23pohamhandle import PohamHandle # 여기 진짜 중요하다. ***********

class PohamCar:
    turnShowMessage = "정지"

    def __init__(self, ownerName):

        # ownerName = ownerName # 이렇게 쓰면 안 됨.
        self.ownerName = ownerName
        self.handle = PohamHandle() # 클래스의 포함관계
        # 포함 핸들의 객체는 self.handle만 알고 있다.

    def turnHandle(self, q):
        if q > 0:
            self.handle.rightTrun(q) # 이렇게 클래스의 def를 가져와라 중요 *******
        elif q < 0:
            self.handle.leftTrun(q) # q를 통해, leftTrun(self, quentity)의 quentity로 감.
        elif q == 0 :
            self.turnShowMessage = "직진"

"""
class PohamHandle:
    quantity = 0 # 핸들 회전량

    def leftTrun(self, quentity):
        self.quantity = quentity
        return "좌회전"
    
    def rightTrun(self, quentity):
        self.quantity = quentity
        return "우회전"
"""

if __name__ == "__main__":      # 돌아가는데, 아무것도 터미널에 없지? 리턴값이 없지?
                                # __name__ == "__name__"
                                # 근데 이건 되네: "__main__" == "__main__"

    tom = PohamCar("미스터 톰")
    tom.turnHandle(10)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + \
        " " + str(tom.handle.quantity)) # "."이 두개라면 포함 관계

    # 기술적인건 상속에 있고.
    # 쓰는건 주로 포함에서 쓴다.


    john = PohamCar("Mr. join")
    john.turnHandle(-20)
    print(john.ownerName + "의 회전량은 " + john.turnShowMessage + \
        " " + str(john.handle.quantity))
    

    john.turnHandle(0)
    print(john.ownerName + "의 회전량은 " + john.turnShowMessage + \
        " " + " 0")


