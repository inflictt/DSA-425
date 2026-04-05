# merge sort - div nd conq
# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
arr = [4, 1, 3, 9, 7,11,2]
# first creatieng merge / combine function 
def mergeCombine(leftArr,rightArr):
    res=[]
    n=len(leftArr)
    m=len(rightArr)
    i,j=0,0
    #compare over len if one gets over break nd direclty add the elm of that array who is bigger in term os length
    while i<n and j<m:
        if leftArr[i]<rightArr[j]:
            res.append(leftArr[i])
            i+=1
        else:            
            res.append(rightArr[j])
            j+=1
    # now check koi si arr mai legnht backgyi kya
    if i<n:
        while i < n :
            res.append(leftArr[i])
            i+=1
    if j<m:
            while j < m:
                res.append(rightArr[j])
                j+=1
    print(res)
    return res


def mergeSort(arr):

    if len(arr)<=1:return arr #case already sorted also base case

    n =len(arr)
    mid = n//2
    leftArr = arr[:mid]
    rightArr = arr[mid:]
    left = mergeSort(leftArr)
    right = mergeSort(rightArr)
    return mergeCombine(left,right)

mergeSort(arr)