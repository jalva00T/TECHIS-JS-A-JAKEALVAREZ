 # FINDING SECOND HIGHEST NUMBER 

print("Please enter # of scores: ")
n = int(input())

print("Please enter individual scores: ")
arr = list(map(int, input().split()))
arr.sort()
print(arr[(arr.index(max(arr)))-1])