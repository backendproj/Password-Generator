from random import shuffle
from string import ascii_letters,digits,punctuation
while True:
    res = []
    print("Iltimos terayotgan parolning uzunligi 8 qator bo'lsin! Oldik🥂")
    letter = int(input("Nechta harf bolishini istaysiz janob: ") )   
    number = int(input("Nechta raqam bo'lishini istaysiz janob: "))
    symbol = int(input("Nechta belgilar bolishini istaysiz janob: "))
    x = list(ascii_letters)
    y = list(str(digits))
    z = list(punctuation)
    shuffle(x)
    shuffle(y)
    shuffle(z)
    while letter > 0:
        res.append(x[letter])                                                           
        letter = letter - 1

    while number > 0:
        res.append(y[number])
        number = number - 1

    while symbol > 0:
        res.append(z[symbol])                                                          
        symbol = symbol - 1

    shuffle(res)   
    string =  "".join(res)
    print(string)

    again = input("Yana generatsiya qilishni istaysizmi? Ha uchun 'H' yo'q uchun 'Y' ni kritishingizni so'raymiz!: ")
    if again.lower() == "h":
        continue
    else:
        print("Oldik unda Thank You🥂")
        break
        




