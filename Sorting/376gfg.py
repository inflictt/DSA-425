# Selection Sort
# Input: arr = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
arr = [4, 1, 3, 9, 7]
n = len(arr)
for i in range(n):
    min_index = i #arr[min_index]=arr[0] now 
    for j in range(i+1,n-1):
        if arr[min_index]>arr[j]:#mtlb curr jo j idx pr elem h woh chota hai min_idx se so update indexs as 4>1
                min_index =  j #now arr[min_index]=arr[1]
    arr[i],arr[min_index] = arr[min_index],arr[i]
print("------ Sorted arr by selction sort ------")
print(arr)
 
# key - agar chota elem aage arr mai hai toh i index par aayega min_index ke through