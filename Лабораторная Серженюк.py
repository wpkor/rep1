t1=input("Введите список товаров:") #в целом я не знаю зачем эта строчка но по условию задачи нужен список товаров
diksi=[]
pyat=[]
mag=[]
pyat.extend(input("Введите цены товаров в Пятёрочке(через запятую без пробелов, максимум 3 товара)").split(","))
mag.extend(input("Введите цены товаров в Магните (через запятую без пробелов, максимум 3 товара)").split(","))
diksi.extend(input("Введите цены через запятую(без пробелов, максимум 3 товара").split(","))
pyatsum=(int(pyat[0])+int(pyat[1])+int(pyat[2]))
magsum=(int(mag[0])+int(mag[1])+int(mag[2]))
diksisum=(int(diksi[0])+int(diksi[1])+int(diksi[2]))
vygoda=min(pyatsum,magsum,diksisum)
print("Цена в Пятёрочке:",pyatsum,"Цена в Магните:",magsum,"Цена в Дикси:",diksisum)
if vygoda == pyatsum:
    print("Дешевле всего будет в Пятёрочке")
elif vygoda == magsum:
    print("Дешевле всего будет в Магните")
elif vygoda == diksisum:
    print("Дешевле всего будет в Дикси")
else:
    print("Ошибка")