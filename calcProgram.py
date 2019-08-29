# 파이썬은 (")와  (') 모두 문자열을 포함하는 기호로 읽는다.
# eval() 함수는 문자로된 수식을 계산하여 결괏값으로 돌려준다.

# make_question 함수
# 1. 랜덤 숫자 두개 만들기
# 2. 덧셈(1), 뺄셈(2), 곱셈(3), 나눗셈(4)중 골라 계산 문제를 완성

# main 프로그램
# 1. 정답/오답 횟수 기록 변수 sr1, sr2
# 2. 0으로 초기화 필요

import random

def make_question():
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    op = random.randint(1, 3) #일단 나눗셈 제외

    q = str(a)

    if op == 1: # 덧셈
        q += "+"
    if op == 2: # 뺄셈
        q += "-"
    if op == 3: # 곱셈
        q += "*"
    if op == 4: # 나눗셈
        q += "/"

    q += str(b)

    return q

# main
sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("정답")
        sc1 += 1
    else:
        print("오답")
        sc2 += 1

print("정답수 :", sc1, "오답수 : ", sc2)
if sc2 == 0:
    print("한번에 맞추셨습니다.")