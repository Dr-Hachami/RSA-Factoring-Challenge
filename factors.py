import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return f"{number}={i}*{number//i}"
    return f"{number}={number}*1"

def main(input_file):
    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        number = int(number)
        factorization = factorize(number)
        print(factorization)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)

