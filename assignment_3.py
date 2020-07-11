num = input("Please enter a positive number :")
strong = len(num)
i = 0
summon = 0
while i < strong:
    digit = int(num[i]) ** strong
    summon += digit
    i += 1
if summon == int(num):
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))
