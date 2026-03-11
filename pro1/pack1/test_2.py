# 입력
# 10
# 0 0 254 185 76 227 84 175 0 0
# 10
# 0 0 251 199 176 27 184 75 0 0
# 11
# 0 0 118 90 243 178 99 100 200 0 0
# ...

# 출력
# #1 111
# #2 60
# #3 165s




import sys
rd = sys.stdin.buffer.readline

T = int(rd().strip())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, X = map(int, rd().split())

    arr = []
    while len(arr) < N:
        arr.extend(map(int, rd().split()))
    
    absX = abs(X)

    if abs == 0:
        0

    dist = 0
    cnt = 0
    while dist < absX:

        for n in arr:
            dist += n
            cnt += 1

    print(cnt)