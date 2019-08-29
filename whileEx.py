# while 숫자 합계 출력
print("[1-10]")
x = 1
while x <= 10:
    print(x)
    x+=1

# 숫자 추측 프로그램
import random

n = random.randint(1, 30)

while True:
    x = input("맞춰보세요")
    g = int(x)
    if g == n:
        print("정답")
        break
    if g < n:
        print("너무 작음")
    if g > n:
        print("너무 큼")
