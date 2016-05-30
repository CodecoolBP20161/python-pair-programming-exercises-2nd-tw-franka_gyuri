import datetime


def years(age):
    now_date = datetime.datetime.now()
    when_100 = now_date.year + 100 - age
    return when_100


def main():
    name = input("What's your name?\n")
    age = int(input("How old are you?\n"))
    how_many = int(input("How many times shall I print the answer?"))
    print(("\nAt this time of year %s you'll be 100 years old." % (years(age))) * how_many)


if __name__ == '__main__':
    main()
