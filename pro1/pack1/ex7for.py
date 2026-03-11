# 반복문 for

#for i in [1,2,3,4,5,6,7]:
for i in (1,2,3,4,5,6,7):
#for i in {1,2,3,4,5,6,7}:
    print(i, end = ' ')

print('분산/표준편차 ----')

numbers = [1,3,5,7,9]
tot = 0
for a in numbers:
    tot += a

print(f"합은 {tot}, 평균은 {tot/len(numbers)}")
avg = tot / len(numbers)

hap = 0
for i in numbers:
	hap += (i - avg) ** 2
print(f"편차 제곱의 합 {hap}")
vari = hap / len(numbers)

print(f"분산은 {vari}")
print(f"표준편자 {(vari) ** 0.5}")

print()

colors = ['r','g','b']

for v in colors:
    print(v, end = ' ')


print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator = iter(colors)

for v in iterator:
    print(v, end = ', ')

print()
for idx, d in enumerate(colors):    #인덱스와 값을 반환
    print(idx, ' ', d)





print('\n사전형 ---')

datas = {'python':'만능언어', 'java':'웹용언어', 'mariadb':'RDBMS'}
for i in datas.items():
    #print(i)
    print(i[0], i[1])

for k, v in datas.items():
    print(k, '--', v)

for k in datas.keys():
    print(k, end = ' ')

for val in datas.keys():
    print(val, end = ' ')

print('다중 for --------')
for n in range(1,10):
    print('--{}단--'.format(n))
    for i in range(1, 16):
        print('{} * {} = {}'.format(n, i, n*i))

print('continue, break -------')


for i_num in range(1, 6):
    if i_num == 2: continue
#    if i_num == 4: break
    print(i_num, end = " ")
else:
    print("정상종료")


print("\n 정규 표현식 + for ")

str = """
퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.
우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.
예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.

교환전>


처음에는 첫번째 숫자판의 3과 네 번째 숫자판의 8을 교환해서 8, 2, 8, 3, 8이 되었다.
 

다음으로, 두 번째 숫자판 2와 마지막에 있는 8을 교환해서 8, 8, 8, 3, 2이 되었다.


정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.
위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.
여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.



94의 경우 2회 교환하게 되면 원래의 94가 된다.
정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

[입력]
가장 첫 줄은 전체 테스트 케이스의 수이다.
최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.
각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

[출력]
각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.
같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.
"""

import re

str2 = re.sub(r'[^가-힣\s]', '', str)   #한글과 공백 이외의 문자는 공백처리
print(str2)
str3 = str2.split(' ') # 공백을 기준으로 문자열을 구분
print(str3)

count = {}

for word in str3:
    
# if word in count:
#     count[word] += 1
# else:
#     count[word] = 1
    count[word] = count.get(word, 0) + 1

print(count)

# ^ 시작을 의미, $ 끝을 의미
print('정규 표현식 좀 더 연습')
for test_ss in ['111-1234', '일이삼-일이삼사','222-1234','333&1234']:
    if re.match(r'^\d{3}-\d{4}$', test_ss):

        print(test_ss, '전화번호 맞아요')

    else:
        print(test_ss, '전화번호 아니야.')


print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
a = [1,2,3,4,5,6,7,8,9,10]

li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
    
print(list(i for i in a if i%2 == 0))

datas = set([1,2, 'a', True, 3.0, 2, 1, 2, 1]) # == {1,2, 'a', True, 3.0, 2, 1, 2, 1} 
li2 = [i*i for i in datas if type(i) == int]

print(li2)

id_name = {1:'tom', 2:'oscar'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)
print()
print([1,2,3])
print(*[1,2,3])
aa = [(1,2), (3,4), (5,6)]
for a, b in aa:
    print(a + b)

print([a + b for a, b in aa])
print(*[a + b for a, b in aa], sep='\n')

print('\n수열 생성 : range')
print(tuple(range(1,6,2)))
print(list(range(-10, -100, -20)))
print(set(range(1, 6)))
print()
for i in range(6):
    print(i, end = ' ')

for _ in range(6):
    print('반복')

tot = 0

for i in range(1, 11):
    tot += i
print('tot : ', tot)
print('tot : ', sum(range(1, 11)))

for n in range(1,10):
    print('--{}단--'.format(n))
    for i in range(1, 16):
        print('{} * {} = {}'.format(n, i, n*i))



# 문1 : 2~9 구구단 출력  (단은 행 단위 출력)
for n in range(1,10):
    print('--{}단--'.format(n))
    for i in range(1, 16):
        print('{}*{}={}||'.format(n, i, n*i), end = ' ')

print()
# 문2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
arr=[]
for cube_1 in range(1,7):
    cube_sum = 0
    for cube_2 in range(1,7):
        cube_sum = (cube_1 + cube_2) 
        if (cube_sum % 4) == 0:
            arr.append(cube_sum)
            print(cube_1, cube_2)

print(f'4의 배수는 {sorted(set(arr))}')

print('\nend')






