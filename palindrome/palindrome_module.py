def palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    gnirts = string[::-1]
    if gnirts == string:
        return True
    else:
        return False


def main():
    text = input("Write something plsss:  ")
    return palindrome(text)


if __name__ == '__main__':
    main()
