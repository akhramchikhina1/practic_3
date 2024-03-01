x=int(input('Введите целое число: '))
y=int(input('Введите целое число: '))
result= int((x%y==0) or (y%x==0))
print(result)