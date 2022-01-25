import math

# SIMPLE CALCULATOR

# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
# 5. SQUARE ROOT
# 6. RAISE THE POWER


print("WELCOME TO THE CALCULATOR")
print("Whatcha wanna do?")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO SECOND POWER")

operation = input()

if operation == "1":
    # code for add
    print("ALRIGHT! Let's do some addition.")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    print("The sum is equal to " + str(int(num1) + int(num2)))
    # print(({num1} + {num2}) + "The sum is equal to " + str(int(num1) + int(num2)))

elif operation == "2":
    # code for subtract
    print("ALRIGHT! Let's do some subtraction.")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    print("The difference is equal to " + str(int(num1) - int(num2)))

elif operation == "3":
    # code for multiply
    print("ALRIGHT! Let's do some multiplication.")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    print("The product is equal to " + str(int(num1) * int(num2)))

elif operation == "4":
    # code for division
    print("ALRIGHT! Let's do some division.")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    print("The quotient is equal to " + str(int(num1) / int(num2)))

elif operation == "5":
    # code for SQUARE ROOT
    print("ALRIGHT! Let's find that square root.")
    num = int(input("Enter Number: "))
    print("The square root is equal to %f " % (math.sqrt(num)))

elif operation == "6":
    # code for raise power
    
    #TEST
    # num = int(input("Enter Number: "))

    #REAL DEAL
    print("ALRIGHT! Let's raise that power.")
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num = num1 + num2
    print(str(num) + " to the second power is %d " % (pow(num, 2)))

else:
    print("Cmon! You can't do that!")