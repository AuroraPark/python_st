# 랜덤 값 이용하여 거북이 그리기
import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500): # 거북이를 오백번 움직인다
    a = random.randint(1, 360) # 1~360 에서 아무수나 골라 a 에 저장한다.
    t.setheading(a)
    b = random.randint(1, 20)
    t.forward(b)

# 랜덤 덧셈 맞추기 프로그램
c = random.randint(1, 30)
d = random.randint(1, 30)
print(c,"+",d,"=")

x = input()
y = int(x)

if y == c + d:
    print("정답!")
else:
    print("오답!")
