#  Bubble Sort 
# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
#adj to be compared
arr = [4, 1, 3, 9, 7]
n = len(arr)
for i in range(0,n-1):
    for j in range(n-i-1):#this is the passes as one elem fixed means we dont have to sort that as biggest gets setteled at right position after every it
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]#swapped
print(arr)
#to ooptimised use a bool flag isSwapped t/f.