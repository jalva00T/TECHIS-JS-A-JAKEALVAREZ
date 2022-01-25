# SWAPPING 2 VARIABLES

# TEST
# x = "hello"
# y = "world"

# REAL DEAL
print("WELCOME TO THE VARIABLE SWAPPER. INPUT TWO VARIABLES AND WATCH THEM SWAP!")

x = input("Input Variable #1: ")
y = input("Input Variable #2: ")

x,y = y,x

print("Variable #2: " + x)
print("Variable #1: " + y)