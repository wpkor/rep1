a=int(input())
if (not(a % 100 == 0) and (a % 4 == 0)) or (a % 400 == 0):
    print("Високосный год")
else:
    print("Обычный год")


