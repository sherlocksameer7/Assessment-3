num = int(input("Enter any Number : "))
min = 9
while num > 0:
    digit = num % 10
    if min > digit:
        min = digit
    num = num // 10
print("Smallest Digit is : ", min)