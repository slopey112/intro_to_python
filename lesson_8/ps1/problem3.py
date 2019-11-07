def pyramid(n):
    for i in range(0, n + 9, 2):
        for j in range(round(i / 2)):
            print("", end=" ")
        for j in range(n - round(i / 2)):
            print(".", end=" ")
        for j in range(round(i / 2)):
            print("", end=" ")
        print()


def main():
    pyramid(10)


if __name__ == "__main__":
    main()
