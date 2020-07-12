num = int(input("Please enter a positive number(except one): "))
i = 2
while (i <= num) and (num % i != 0):
    i += 1
if num == i:
    print("{} is a prime number.".format(num))
else:
    print("{} is not a prime number.".format(num))
