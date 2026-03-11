
a = 1

while a <= 5:
    print(a, end = ' ')
    a += 1

else:
    print('수행성공')

print()

i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i=' + str(i) + '   j=' + str(j))
        j += 1
    i +=1


N = 100

num = 0; ans = 0
while num <= 100:
    num += 1

    if (num % 3) == 0:
        ans += num

print('합은 ', ans)

print('1~100 사이의 정수 중 3의 배수의 합')


print()
colors = ["빨강", "파랑", "노랑"]

num_color=0
#while num_color < 3:

while num_color < len(colors):
    print(colors[num_color])

    num_color +=1



print('\n별 찍기 -------')

star_col = 1
spr = 30
while star_col < 30:
    star_row =1
    spare_msg = " " * spr
    msg=''
    while star_row <= star_col:
        msg += "*"
        star_row += 1
    print(spare_msg + msg)
    star_col += 2
    spr -= 1







print("if 블록 내 while 블록 사용 ------")

"""
import time


sw = input('폭탄 스위치를 누를까요?[y/n]')

if sw == 'Y' or sw == 'y':
    print("sw : ", sw)
    count = 5
    while 1 <= count:
        print('%d초 남았습니다' %count)
        time.sleep(1)  # 1초 후 다음 문장을 실행
        count -= 1
    print('폭발')
    pass
elif sw == 'N' or sw == 'n':
    print('작업 취소')
else:
    print('y 또는 n을 누르세요.')

print("\ncontinue/break ---")
"""


a = 0
while a < 10:
    a += 1
    if a == 3 :continue # 아래 문을 무시하고 다음 반복문을 실행.
    if a == 5 :continue
    if a == 7 :break
    print(a)
else:
    print('정상종료')

print('while 수행 후 %d' %a)

print('\n키보드로 숫자를 입력받아 홀수 짝수 확인하기 (무한 반복)---')


while True:
    num = float(input('숫자를 눌러라'))
    if (num % 2) == 0:
        print ("%d는 짝수" %num)
    elif (num % 2) == 1:
        print ("%d는 홀수" %num)
    else:
        print("정수가 아님")

print('end')