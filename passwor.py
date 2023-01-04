from random import randint
from random import shuffle
from string import ascii_letters,punctuation , digits
import random

def password():
    while True:
        harflar = int(input("Nechta harf bo'lsin? "))
        belgilar = int(input("Nechta belgi bo'lsin? "))
        raqamlar = int(input("Nechta raqam bo'lsin? "))
        
        list = []
        for harflar in range(0 , harflar):
            a = randint(0 , 53)
            harf = ascii_letters[a]
            list.append(harf)

        for belgilar in range(0 , belgilar):
            a = randint(0 , 9)
            belgi = digits[a]
            list.append(belgi)

        for raqamlar in range(0 , raqamlar):
            a = randint(0 , 9)
            raqam = digits[a]
        
            list.append(raqam)
        print(list)

        qaytar = input("Yana parol yaratishimizni hohlaysizmi? Agar Ha bo'lsa H ni bosing  Yo'q bo'lsa Y ni bosing deb javob berin:")
        if qaytar.lower() == "h":
            continue
        else:
            break

print(password())