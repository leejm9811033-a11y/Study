import sys
sys.stdin = open("1_sample_input.txt", "r")
rd = sys.stdin.buffer.readline

T = int(rd().strip())
out = []

for tc in range(1, 2):
    s = rd().strip().decode()   # 예: "131003"
    print(f"\n[TC {tc}] 입력 문자열 s = {s}")

    first = [-1] * 10   # first[d] : 숫자 d가 "처음" 등장한 위치(i)를 저장 (아직 안 나오면 -1)
    count = [0] * 10    # count[d] : 숫자 d가 지금까지 몇 번 나왔는지 카운트

    ok = True

    # s를 왼쪽부터 한 글자씩 읽는다.
    for i, ch in enumerate(s):

        d = ord(ch) - ord('0')  # 더 직관적으로 ord('0') 사용
        print(f"  i={i}, ch='{ch}', d={d}")

        # 등장 횟수 증가
        count[d] += 1
        print(f"    count[{d}] 증가 -> {count[d]}")

        # 1번째 등장: first에 위치 저장
        if count[d] == 1:
            first[d] = i
            print(f"    '{d}' 첫 등장! first[{d}] = {i}")

        # 2번째 등장: 거리 조건 검사
        elif count[d] == 2:
            gap = i - first[d] - 1  # 두 숫자 사이에 있는 문자 개수
            print(f"    '{d}' 두 번째 등장! 첫 위치={first[d]}, 현재 위치={i}, 사이 개수(gap)={gap}")

            # 조건: 사이에 있는 문자 개수 == d
            if gap != d:
                print(f"    [FAIL] gap({gap}) != d({d}) 이므로 조건 위반!")
                ok = False
                break
            else:
                print(f"    [OK] gap({gap}) == d({d}) 조건 만족!")

        # 3번째 이상 등장: 즉시 실패
        else:
            print(f"    [FAIL] '{d}'가 3번 이상 등장함! (count[{d}]={count[d]})")
            ok = False
            break

        # 중간 상태를 눈으로 보기 좋게 출력 (원하면 주석처리 가능)
        print(f"    현재 first = {first}")
        print(f"    현재 count = {count}")

    # 여기까지 왔다는 건 "거리 조건"과 "등장 3회 이상"은 문제 없었다는 뜻.
    # 이제 "0 또는 2번 등장" 조건을 최종 확인해야 함.
    if ok:
        print("  [최종 체크] 어떤 숫자가 1번만 등장했는지 확인...")
        for d in range(10):
            if count[d] == 1:
                print(f"    [FAIL] 숫자 {d}가 1번만 등장함!")
                ok = False
                break

    result = "yes" if ok else "no"
    print(f"[TC {tc}] 결과 = {result}")
    out.append(result)

print("\n--- 최종 출력 ---")
print("\n".join(out))
print("\n\n\n\n\n\n\n\n\n")