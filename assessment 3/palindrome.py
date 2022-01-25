# FINDING PALINDROME

print("WELCOME TO THE PALINDROME IDENTIFIER. ENTER A VALUE AND SEE IF IT IS? ")

input = input("Enter ANY value: ")

reverse = input[::-1] # slice the input
                      # "::" doesn't specify a starting or ending point so the entire string is sliced
                      # "-1" reverses the string

if( input == reverse ):
    print("OH YEA! " + input + " IS a palindrome.")
else:
    print("Nope! " + input + " IS NOT a palindrome, bud. ")