# 단순 반복문
for x in range(10):
    print("hello")

# 블록 반복문
for x in range(3):
    print(100)
    print(200)
print(300)


# 반복문 숫자 리스트 - 마지막수 미포함
for x in range(1, 11):
    print(x)

# 반복문 합계(SUM)
s = 0
for x in range(1, 10+1):
    s = s + x # s += x 도 가능
    print("x:", x, " s:", s)

# 원그리기
import turtle as t

n=50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)