
# 1122. Relative Sort Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr2copy = set(arr2)
arr1Count = dict()
remElem = []
ans = []
for n in arr1:
    if n not in arr2copy:
        remElem.append(n)
    arr1Count[n]=arr1Count.get(n,0)+1#this build the value of key:pair like  number:occurences and giveus cometplte dict off arr1 same as colelction counter 
remElem = sorted(remElem) #sorts the leftover elems

for val in arr2:
    for _ in range(arr1Count[val]):#kitni baar chalna hai woh ye batayga arr1Count[val] eg.val =2 arr1count[2]=3 thts the no of time 2 occured
        ans.append(val)#loops run thrice. adn append 2 three time [2,2,2]
ans.extend(remElem)#in the end we got our ans list and now lefover elem to be added so its fixed 
print (ans)
