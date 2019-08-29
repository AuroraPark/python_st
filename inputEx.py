# 문자열 입력받기
name = input("your name?")
print("hello", name)

# 숫자 입력받아 곱셈 출력하기
x = input("?")
a = int(x)

y = input("?")
b = int(y)

print(a * b)

# 20초 맞히는 프로그램
import time

input("엔터를 누르고 20초를 셉니다")
start = time.time()

input("20초 뒤에 다시 엔터를 누릅니다")
end = time.time()

et = end - start # 실제 걸린 시간 구하기
print("실제 시간 : ", et , "초")
print("차이 : ", abs(et - 20), "초") # abs 절대값