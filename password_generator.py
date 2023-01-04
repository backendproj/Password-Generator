import random
import string

def password_generator():
    harflar = int(input("Parlollar generatsiyasida nechta harf qatnashsin: "))

    belgilar = int(input("Parlollar generatsiyasida nechta belgi qatnashsin: "))

    raqamlar = int(input("Parlollar generatsiyasida nechta raqam qatnashsin: "))

    password_list = []

    for i in range(harflar):
        letter = random.choice(string.ascii_letters)
        password_list.append(letter)

    for i in range(belgilar):
        character = random.choice(string.punctuation)
        password_list.append(character)

    for i in range(raqamlar):
        number = random.randint(0,9)
        password_list.append(str(number))

    random.shuffle(password_list)

    password = ''.join(password_list[:])

    print("Sizning parolingiz: ", password)

password_generator()