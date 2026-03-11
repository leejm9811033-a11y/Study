
class CoinIn:
    def __init__(self, coin):
        self.coin = coin
        self.change = 0

    def culc(self, cup_count, price_per_cup=200):
        need = cup_count * price_per_cup

        if self.coin < need:
            shortage = need - self.coin
            return False, shortage
        else:
            self.charge = self.coin - need
            return True, self.charge
        
class arr_list:
    def __init__(self):

        self.out = []

    def arr(self, coin, cup_count, result, ok):

        self.out =[]

        self.out.append(f"동전을 입력하세요 : {coin}")
        self.out.append(f"몇 잔을 원하세요 : {cup_count}")

        if ok:
            self.out.append(f"커피 {cup_count}잔과 잔돈 {result}원")
        else:
            self.out.append(f"요금이 부족합니다. {result}")

        return self.out

class Machine:
    def __init__(self):
        self.cupCount = 1
        self.out = []

    def showData(self):

        coin = int(input("insert the coin : "))
        cup_count = int(input("How many cups do you want? "))

        self.cupCount = cup_count

        coin_in = CoinIn(coin)

        ok, result = coin_in.culc(cup_count)

        a = arr_list.arr(self, coin, cup_count, result, ok)

        return a

if __name__ == "__main__":

    m = Machine()
    print("\n".join(m.showData()))
