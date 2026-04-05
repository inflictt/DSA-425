# quick sort - partition
# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
arr = [2, 8 , 4, 1, 3, 9, 7]
n = len(arr)
def partition(arr,low,high):
    i=low
    j = high
    pivot = arr[low]
    while i < j  :#should stop when i overlaps j so we swap j. and pivot
        pivot =arr[low]
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j 

def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        p_index = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)

# partition finction : 
# 1. make pivout as arr[low] changes with its made and then run loop with i from start and j from back 
# 2. i finding and elem bigger than pivot and j finding and elem less than pivot
# 3.and if i<j and outer loop still running swap inside aand then follow the same
# 4. and if the loop is over we nnow know thart j is the required index of pivout means arr[low] and return j thne 