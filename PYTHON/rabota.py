# summa=0
# NumberofDigits=int(input('Введите количество чисел: '))
# for i in range(NumberofDigits):
#     Number=int(input('Введите число: '))
#     if Number%6==0:
#         summa+=Number
# print(summa)
# kol=0
# NumberofDigits=int(input('Введите количество чисел: '))
# for i in range(NumberofDigits):
#     Number=int(input('Введите число: '))
#     if Number%4==0:
#         kol+=1
# print(kol)
summa=0
pol=0
neg=0
dif=0
Number=1
while Number!=0:
    Number=int(input('Введите число: '))
    summa+=Number
    if Number>0:
        pol+=1
    if Number<0:
        neg+=1
    dif=pol-neg
print(summa)
print(dif)

    


