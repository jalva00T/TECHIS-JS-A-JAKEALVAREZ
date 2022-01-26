# SYMMETRIC DIFFERENCE

print("Standard Inputs")
print("#1. 4")
print("#2. 2 4 5 9")
print("#3. 4")
print("#4. 2 4 11 12")

print("Please enter standard input #1: ")
n = int(input())

print("Please enter standard input #2: ")
set1 = set(map(int, input().split()))

print("Please enter standard input #3: ")
m = int(input())

print("Please enter standard input #4: ")
set2 = set(map(int, input().split()))

set3 = set1.union(set2)

list = []
for i in set3:
    if i in set1 and i in set2:
        pass
    else:
        list.append(i)

print("Here's your ascending symmetric difference list: ")

list.sort()
for i in list:
    print(i)
