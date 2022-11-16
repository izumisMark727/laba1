a=int(input())
b=int(input())
c=int(input())
if a==0:
    print(-1*c/b)
elif b**2-4*a*c>=0: #проверка неотрицательности дискриминанта
    x1=(-1*b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(b*(-1)-(b**2-4*a*c)**0.5)/(2*a) #2 формулы для корней
    print(x1,x2)
else:
    print("No real roots")
