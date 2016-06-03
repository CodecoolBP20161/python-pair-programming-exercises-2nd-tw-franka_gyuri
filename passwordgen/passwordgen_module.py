import random


def weak_password():
    word_list = []
    with open('README.txt', 'r') as w:
        for line in w:
            for word in line.split(' '):
                word_list.append(word)
    word_1 = word_list[random.randint(0, len(word_list))]
    word_2 = word_list[random.randint(0, len(word_list))]
    while word_1 == word_2:
        word_2 = word_list[random.randint(0, len(word_list))]
    password = word_1 + ' ' + word_2
    return password


def passwordgen(length=8):
    length = int(input("Pick a length for your password(min 8 characters)!\n"))
    if length < 8:
        length = int(input("Password should be minimum 8 characters you freak!\nChose another!\n"))
    character_lists = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!@#$%^&*()?']
    while True:
        password = ''
        used = [False, False, False, False]
        all_used = [True, True, True, True]
        for i in range(length):
            a = random.randint(0, 3)
            used[a] = True
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            password += s[b]
        if used == all_used:
            break
    return password


def main():
    star_wars = input("Enter 's' for strong password or 'w' for a weak one:\n")
    if star_wars == "s":
        print(passwordgen())
    elif star_wars == "w":
        print(weak_password())
    else:
        print("It's 's' or 'w', dummy!\n")
        main()
    return


if __name__ == '__main__':
    main()
