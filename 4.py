quantity=str(input('Введите цену латте в рублях, копейках и количество чашек: '))
quantity=quantity.split(' ')
price_rubles=int(quantity[0])
price_k=int(quantity[1])
quantity=int(quantity[2])
TR_k=(price_rubles*100+price_k) * quantity
TR_r= TR_k//100
ost_k=TR_k % 100
print(TR_r, 'руб.', ost_k, 'коп.')
