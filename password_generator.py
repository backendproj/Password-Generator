from random import shuffle , randint
from string import ascii_letters , digits , punctuation

list = []
def password():
    letters = int(input(" Parolingiz nechta xarifdan iborat bolsin : "))
    numbers = int(input(" Parolingiz nechta belgidan iborat bolsin : "))
    symbols = int(input(" Parolingiz nechta raqamdan iborat bolsin : "))

    for _ in range(letters):
        list.append(ascii_letters[randint(0, len(ascii_letters)-1)])

    for _ in range(numbers):
        list.append(digits[randint(0, len(digits)-1)])

    for _ in range(symbols):
        list.append(punctuation[randint(0, len(punctuation)-1)])

    shuffle(list)

    password = ""

    for  x in list:
        password = password + str(x)
    print(f"Sizning parolingiz quidagicha : {password} ")


    if len(list) >= 8:
        return"sizning parolingiz mustaxkam boldi !"
    else:
        return"Siznig  parolingiz yaroqsiz ozgartrishingiz tavsiya qlaman"



while True:
    print(password())
    povtor = input('''Yana urinib korishni uchun 'Y' bosing 
        Toxtatish uchun 'N' bosin : ''')
        
        
    if povtor.lower() == "y" :
        continue
    else:
        print("Kep turing !")
        break

