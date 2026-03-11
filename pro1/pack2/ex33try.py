# 예외처리 : 파일, 네트워크, DB작업, 실행 에러 등의 에러 대처

def divide(a, b):
    return a / b



print("이런 저전 작업 진행...")

# c = divide(5, 2)
# print(c)

# c = divide(5, 0) # ZeroDivisionError: division by zero
# print(c)

try:
    # 실행문 (예외 발생 가능 구문)
    c = divide(5, 2)
    # c = divide(5, 0)
    print(c)

    aa = [1, 2]
    print(aa[0])
    # print(aa[3])    # IndexError: list index out of range


    open("c:/work/abc/.txt")    # FileNotFoundError: [Errno 2] No such file or directory: 'c:/work/abc/.txt'


    pass

# python exception 종류
except ZeroDivisionError:   # 예외 종류 관련 클래스
    print("두번째 값은 0을 주면 안 됩니다.")    # 예외 발생 처리 구문

except IndexError as err:
    print("참조 범위 오류 : ", err)

except Exception as e:  # error 관련 클래스의 최상위
    print("에러 : ", e)     # except 순서 위치를 주의

finally:
    print("에러 유무에 상관없이 반드시 수행됨")




print("end")













