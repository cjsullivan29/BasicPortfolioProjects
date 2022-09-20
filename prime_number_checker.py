#Prime nubmer checker

number = int(input("Check this number: "))


def prime_num_checker (number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime == False
    if is_prime:
        print("It's prime.")
    else:
        print("It's not prime.")

print(prime_num_checker(number))