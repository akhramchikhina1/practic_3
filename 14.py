n=float(input('Введите число градусов: '))
hours= int(n//30)
minutes=int(n%30)*2
print(hours, 'часов', minutes, 'минут')