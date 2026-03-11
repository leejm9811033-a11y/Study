# 연산자
v1 = 3        # 치환 연산자
v1 = v2 = v3 = 5
print(v1, v2, v3)
print('출력1', end = ' ')
print('출력2')
print('출력3')

v1, v2 = 10, 20   # overwrite 가 아니라서, 변수 스왑 가능
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5    # v1 = (1,2,3,4,5) 튜플이군!!!! 중요

v1 = [1,2,3,4,5]

*v1, v2 = [1,2,3,4,5]    # *은 에스타리스크
print(v1, ' ', v2)


*v1, v2 = [1]             # q, stack이 생각나네?!
print(v1, ' ', v2)

# v1, v2* = [1,2,3,4,5]  # SyntaxError: invalid syntax
print(v1, ' ', v2)

*v1, v2, v3 = [1,2,3,4,5]   
print(v1, ' ', v2, ' ', v3)


v1 = complex(5j)

print(v1)

print()
print(format(1.5678, '10.3f'))   # 전체 10자리 중에 소수 3번째까지 보여줘. 그리고 앞에 공백을 배치
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
abc = 123
print(f"abc의 값은 {abc}임")
print('\t\n\t\b\b\b\b\b\b\b\b본격적 연산 ----------')
print('\t\n\t\b본격적 연산 ----------')  # \n,\b, \t
print('\t\n\t본격적 연산 ----------')    # \t == 8 * \b
print(5+3, 5-3, 5*3, 5/3, 5//3, 5%3, 3**3)

print(divmod(5, 3), ' ', 5%3)
result = 3 + 4 * 5 + (2 + 3) / 2
print(result)


print(5 > 3, 5 == 3, 5 != 3)


print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))

print(True or False and False)
print(True and False or False)

print(4 + 5) # 산술연산
print('4' + '5')  #문자열 더하기 

print('한' + '국' + '만세')
print('한국 ' * 5) 

print('누적')

a = 10
a = a + 1
print(f"a는 {a}")

a += 1   # -=, /= 
print(f"a는 {a}")


print("ABC\bD")

# print(a--) 증감 연산자 없음

print(--a)  # 부호 변경으로 가능
print(-a * -1)

print(int('1' + '1') + 1)
print(float('1' + '1') + 1)
print(complex('j') + 1)
print('boolean 처리 : ', bool(True), bool(False) )
print(str(1 + 1) + '1')
print(bool(1), bool(12.3), bool('ok'), bool([12])) # 다 True
print(bool(0), bool(0.0), bool(''), bool(None)) # 다 True

print('aa\tbb')
print('aa\bbb')
print(r'aa\tbb')
print(r'aa\bbb')

print(bin(1<<10))  # 100000

arr=0
FULL = 1<<3
for num in range(9):
    arr |= ( 1 << num)
    print (bin(arr), '10.3f')

print(bool(0.1))



print(format(1.5678, '10.3f')) 


