# 오버라이딩 : 결제 시스템
# 


class Payment:    # 공통 규칙 선언              # super class
    def pay(self, amount):
        print(f"결제처리 : {amount}원")

# Payment의 자식은 결제를 pay()라는 동일 메소드를 이용하기를 기대
# 동일 인터페이스 구사 

class CardPayment(Payment):
    # 얘만의 고유 멤버 ...

    def pay(self, amount):
        print(f"{amount}원 카드 결제 승인 완료함")

class CashClass(Payment):
    # ...
    def pay(self, amount):
        print(f"{amount}원 현금 결제 완료함 - 감사합니다.")

payments = [CardPayment(), CashClass()]

for p in payments:
    p.pay(5000)     # 이것이 다형성이다.

# 다중 상속 : 부모가 두 군데 이상인데, 상속받음.



