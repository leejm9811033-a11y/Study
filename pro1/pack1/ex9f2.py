# 사용자 정의 함수

"""
def 함수명(가인수,,,):
    return 반환값   # 1개만 반환, return이 없으면 return None

함수명(실인수,,,)   # 함수 호출
"""

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name : ', name)
    return None

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return

def doFunc4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return
    else:
        return imsi


doFunc1()
print("함수 주소는 ", doFunc1)
print("함수 주소는 ", id(doFunc1))
imsi = doFunc1
imsi()
print(doFunc1())
print("---------------")
doFunc2(7)
doFunc2('윌리' + '  ' + '순신')
print("---------------")

doFunc3("대한","민국")
print(doFunc3("대한","민국"))
print(doFunc3(5,6))
#doFunc3("5","6")
result = doFunc3("5", "6")
print(result)

print(doFunc4(3, 4))
print(doFunc4(3, 5))

print('----------------')

def triArea(a, b):
    c = a * b / 2
    triAreaPrint(c)     # 다른 함수 호출

def triAreaPrint(cc):
    print('삼각형의 면적은 ', cc)

triArea(20, 30)

print('----------------')

def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20, 20):
    print('합격')
else:
    print('불합격')

print()

def swapFunc(a, b):
    return b, a     # return (b, a)

a = 10; b = 20
print(a, ' ', b)
print(swapFunc(a, b))

print()

def funcTest():
    print('funcTest 멤버 처리')
    def funcInner ():
        print('내부 함수')
    funcInner()

funcTest()

# if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1    # 홀수이면 True 반환

mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)


print('변수의 생존 범위 (scope rule) ------- ')
# 변수가 저장되는 이름공간은 변수가 어디서 선언 되었는가에 따라 생존 시간이 다름.
# 전역, 지역 변수
player = '전국대표'     # 전역변수 (현재 모듈 어디서든 호출 가능)
name = '한국인'
def funcSoccer():
    name = '홍길동'     # 지역변수 (현재 함수 내에서만 호출 가능)
    # player = '지역대표'
    city = '서울'
    print(f"이름은 {name} 수준은 {player}")
    print(f"지역은 {city}")

funcSoccer()
print(f"이름: {name} 수준: {player}")
# print(f"지역은 {city}")



# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력

num = 0
num_sum = 0
while num <= 100:
    num += 1
    if (num % 3) == 0 and (num % 2) != 0:
        print(num, end = " ")
        num_sum += num
print()
print(f"문1의 답 {num_sum}")

# 문2) 2 ~ 5 까지의 구구단 출력

# 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력

tot = 0
for num in range(1, 101):
    if (num % 2) == 0:
        tot += num
    else:
        tot -= num

print(f"문3의 답 : {tot}")

# 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
tot_odd = 0
for num in range(1, 100, 2):
    if (num % 4) == 1:
        tot_odd -= num
    elif (num % 4) == 3:
        tot_odd += num

print(f"문4의 답 : {tot_odd}")

# 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력

arr = []
for num in range(1, 101):
    num_sum = 0
    for ch in str(num):
        num_sum += int(ch)

    if num_sum >= 10:
        arr.append(num)

print(f"문5의 답 : " + " ".join(map(str, arr)))
# 예) 29 → 2 + 9 = 11 (출력)

# 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
sum_start = 0
num = 0
while sum_start < 1000:
    num += 1
    sum_start += num
print(f"문6의 답 : {num} {sum_start}")
# 힌트: 언제 멈출지 미리 모름 → while 적합


# 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
print(f"문7의 답 : ")
for fir_num in range(1, 10):
    sum_30 = 0
    for sec_num in range(1, 10):
        sum_30 = fir_num * sec_num
        if sum_30 >= 30:
            break
        print(f"{fir_num} * {sec_num} = {sum_30}")


# 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력

primes = [2, 3, 5, 7]

for num in range(11, 1001):  # 10부터가 아니라 11부터 시작하는 게 자연스러움
    is_prime = True
    for p in primes:
        if p * p > num:
            break
        if num % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("소수:", " ".join(map(str, primes)))
print(f"소수의 갯수 : {len(primes)}")


# 힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.

# 그래서 while 안에 while 구조가 필요하다.




a = 10; b = 20; c = 30

def Foo():
    a = 7   # 지역변수
    def Bar():
        global c    # Bar 함수의 멤버가 아니라 모듈(파일)의 멤버가 됨. 전역변수
        nonlocal a
        b = 8   # 지역변수
        print(f"함수 수행 전 a:{a}, b:{b}, c:{c}")
        c = 9
        print(f"함수 수행 중 a:{a}, b:{b}, c:{c}")
        b=100
    Bar()

Foo()
print(f"함수 수행 후 a:{a}, b:{b}, c:{c}")


print()
g = 1
print('g : ', g)
def func():
    # global g
    g = 2
    a = g
    return a

print(func())
print('g : ', g)
