# insertion sort
# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# left sorted | right unsorted 
arr = [4, 1, 3, 9,2 ,11,7]
#main while loop condittion
for i in range(1,len(arr)):
    key = arr[i]#store kr lo as jb j+1 mai aage dhakelengey values toh nums[i] kho na jaaye isliye store it in key
    j = i-1#just pehele ki check krte jaeyngey
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j] #jo val thi ab woh toh overwrite hogyi 
        j-=1
    arr[j+1] = key  #jo key save karaayi uski right pos pr place hogyi ab woh 
print(arr)