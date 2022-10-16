number = int(input("Enter a number: "))

digits = []

while number > 0:
    digit = number % 10
    digits = [digit] + digits
    number = number // 10

print(digits)