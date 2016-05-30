def fizzbuzz(number):
    print_num = number
    if number % 15 == 0:
        print_num = "FizzBuzz"
    elif number % 3 == 0:
        print_num = "Fizz"
    elif number % 5 == 0:
        print_num = "Buzz"
    return print_num


def main():
    for i in range(1, 101):
        fizzbuzz(i)
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
