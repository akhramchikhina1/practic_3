att=float(input('Введите att игрока: '))
comp=float(input('Введите comp игрока: '))
yds=float(input('Введите yds игрока: '))
td=float(input('Введите td игрока: '))
int=float(input('Введите int игрока: '))
passer_rating=(((((((comp/att)-0.3)*5)+(yds/att)-3)*0.25)+(td/att)*20+2.375-(int/att)*25)/6)*100
print(passer_rating)