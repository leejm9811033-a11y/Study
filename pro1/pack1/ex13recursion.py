# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리

def countDown(n):
    if n == 0:
        print("완료")
    else:
        print(n, end = " ")
        countDown(n - 1)    # 재귀

countDown(5)

print("--1 부터 n까지 합 ----------")
def totFunc(n):
    if n == 0:
        print("탈출")
        return 2
    return n + totFunc (n - 1)  # 재귀

result = totFunc(5)
print("result : ", result)
print("--5 factorial(계승)--------")
def factFunc(a):
    if a == 1: return 1
    print(a)
    return a * factFunc(a - 1)

result2 = factFunc(5)
print("result2 : ", result2)

print("end")




"""

def solve():
    s = "asdfasdfsafhasfd"	# byte => str
    bomb = "asdf"  # byte => str

    print(f"1 {bomb[-3:]}")
    print(f"1 {len(bomb)}")

    bomb = list(bomb)
    len_b = len(bomb) # int
    last_b = bomb[-1] # str

    print(f"2 {bomb[-3:]}")
    print(f"2 {len(bomb)}")

    stack = []
    for ch in s:
        stack.append(ch)    


        if len(stack) >= len_b and last_b == stack[-1]:
            if bomb == stack[-len_b:]:
                del stack[-len_b:]


    results = "".join(stack) # stack은 단일 str들의 연속이 모인 리스트
    print(results if results else "FLURA")

if __name__ == "__main__":
	solve()

"""











