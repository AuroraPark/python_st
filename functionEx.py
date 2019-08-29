# 함수 정의
def square(a): # a의 제곱을 구하는 함수
    c = a * a
    return c

def triangle(a, h): # 삼각형 넓이 구하는 함수
    c = a * h / 2
    return c

s1 = 4
s2 = square(s1)
print(s1, s2)

print(triangle(3,4))

# 함수 응용
def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return s

print(sum_func(10))
print(sum_func(100))

# 팩토리얼 함수
def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact

print(factorial(5))
print(factorial(10))

# 다각형을 그리는 함수
import turtle as t
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360 / n)

polygon(3) # 삼각형 그리기
polygon(5) # 오각형 그리기

t.up()
t.forward(100)
t.down()

polygon2(3, 75)
polygon2(5, 100)

t.mainloop() # 프로그램이 바로 종료될 경우 사용하는 명령어

