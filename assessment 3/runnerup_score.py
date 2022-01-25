 # FINDING RUNNER UP SCORE 

print("Please enter # of scores: ")
n = int(input())

print("Please enter individual scores: ")
arr = list(map(int, input().split()))
arr.sort()
print("The runner up score is: " + arr[(arr.index(max(arr)))-1])