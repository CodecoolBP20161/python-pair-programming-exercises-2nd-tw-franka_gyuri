import random


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
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
