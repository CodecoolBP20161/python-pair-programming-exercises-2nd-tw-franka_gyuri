import random


def listoverlap(list1, list2):
    return list(set(list1) & set(list2))


def randomlist():
    c = []
    for i in range(random.randint(5, 20)):
        c.append(random.randint(1, 99))
    return c


def main():
    a = sorted(randomlist())
    print("List1:\n" + str(a))
    b = sorted(randomlist())
    print("List2:\n" + str(b))
    print("Overlap:\n" + str(sorted(listoverlap(a, b))))


if __name__ == '__main__':
    main()
