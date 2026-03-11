
class CoinIn:
    def __init__(self, coin):
        self.coin = coin
        self.change = 0

    def culc(self, cup_count, price_per_cup=200):
        need = cup_count * price_per_cup

        if self.coin < need:
            shortage = need - self.coin
            return False, shortage  # 구매 실패, 부족 금액
        else:
            self.change = self.coin - need
            return True, self.change  # 구매 성공, 잔돈


class Machine:
    def __init__(self):
        self.cupCount = 1  # 기본값(필요하면 사용)
        self.out = []

    def showData(self):
        self.out = []  # 호출할 때마다 출력 초기화

        coin = int(input("동전을 입력하세요 : "))
        cup_count = int(input("몇 잔을 원하세요 : "))

        self.cupCount = cup_count  # 클래스 다이어그램의 cupCount 반영

        coin_in = CoinIn(coin)  # Machine이 CoinIn을 포함(Composition)

        ok, result = coin_in.culc(cup_count)

        self.out.append(f"동전을 입력하세요 : {coin}")
        self.out.append(f"몇 잔을 원하세요 : {cup_count}")

        if ok:
            self.out.append(f"커피 {cup_count}잔과 잔돈 {result}원")
        else:
            self.out.append(f"요금이 부족합니다. {result}원이 더 필요합니다.")

        return self.out


if __name__ == "__main__":
    m = Machine()
    print("\n".join(m.showData()))



"""
조건
입력자료는 키보드를 사용
커피는 한 잔에 200원
100원 넣고 커피를 요구하면 요금 부족 메시지 출력
400원 넣고 2잔 요구하면 두 잔 출력
500원 넣고 1잔 요구하면 300원 반납

출력 형탱 -----------
동전을 입력하세요 : 400
몇잔을 원하세요 : 2
커피 2잔과 잔돈 0원
"""

