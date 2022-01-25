# Capitalize First and Last Name

# Splits strings, makes first letter capital, joins strings back together
def solve(s):
    return ' '.join(i.capitalize()  for i in s.split(' '))

# makes user inout arguement for solve()
s = input("Please enter your first and last name with no capital letters: ")

# variable with result
result = solve(s)

#print variable
print(result)