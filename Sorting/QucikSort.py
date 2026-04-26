def partition(nums, lo, hi):
    i = lo
    j = hi
    pivot = nums[lo]
    while i < j:
        while i <= hi-1 and nums[i] <= pivot:
            i += 1
        while j >= lo+1 and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[lo], nums[j] = nums[j], nums[lo]
    return j  # j isiliey kyukni j par he humara pivot elem hai mtlh j he humara piv indewx h


def quickSort(nums, lo, hi):
    if lo < hi:
        pivInd = partition(nums, lo, hi)
        quickSort(nums, lo, pivInd-1)
        quickSort(nums, pivInd+1, hi)


nums = [10, 13, 3, 14, 6, 0, 1, 5]
n = len(nums)
ans = quickSort(nums, 0, len(nums)-1)
print(nums)
