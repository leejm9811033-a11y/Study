# 통계량 : 데이터의 특징을 하나의 숫자로 요약한 것.
# 표본 데이터를 추출해 전체(모집단) 데이터를 짐작 가능.
# 평균, 분산, 표준 편차 ...


# sample data 평균

#  sqrl{(sum(sample - mean)제곱)/n}

grades = [1, -3, -2, 4]  # 변량  

def show_grades(grades):
    for g in grades:
        print(g, end = " ")


show_grades(grades)
print()
def grades_sum(grades):
    tot = 0

    for g in grades:
        tot += g   
    return tot


def grades_ave(grades):
    ave = grades_sum(grades) / len(grades)
    return ave

# 분산(편차 제곱 평균) -> 평균 값 기준으로 다른 값 들의 흩어진 정도 
def grades_variance(grades):
    ave = grades_sum(grades) / len(grades)
    vari = 0

    for su in grades:
        vari += (su - ave) ** 2
    return vari / len(grades)
    # return vari / (len(grades) - 1)   # “분산을 과소추정하는 걸 보정하기 위해서”


def grades_standard_variace(grades):
    return grades_variance(grades)/len(grades) ** 0.5

print('표준편차는 ', grades_standard_variace(grades))


print('\n넘파이 진원 함수 사용')
import numpy
print("합 ", numpy.sum(grades))
print("평균 ", numpy.mean(grades))
print("분산 ", numpy.var(grades))
print("표준편차 ", numpy.std(grades))








