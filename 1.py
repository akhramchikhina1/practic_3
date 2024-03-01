bitkoin_rubles =float(input('Введите стоимость биткоина в рублях '))
bitkoin_rubles_str=str(bitkoin_rubles)

if len(bitkoin_rubles_str)>=3:
    third_number=bitkoin_rubles_str[-3]
    print(third_number)
else:
    print('Стоимость биткоина меньше трех цифр')