# # 1. Bucket ke andar sort karne ke liye apna custom Insertion Sort
# def custom_insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         # Number ko uski sahi jagah par khiskate jao
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # 2. Main Bucket Sort Function
# def ultimate_bucket_sort(arr):
#     n = len(arr)
#     # Agar 0 ya 1 element hai, toh wo pehle se sorted hai
#     if n <= 1:
#         return arr

#     # A. Min aur Max find karna (FROM SCRATCH)
#     min_val = arr[0]
#     max_val = arr[0]
#     for num in arr:
#         if num < min_val:
#             min_val = num
#         if num > max_val:
#             max_val = num

#     # Agar saare elements same hain (e.g., [5, 5, 5]), toh return kar do
#     if min_val == max_val:
#         return arr

#     # B. N empty buckets create karna
#     # Agar array mein 5 elements hain, toh 5 buckets banengi (Index 0 se 4)
#     buckets = [[] for _ in range(n)]

#     # C. Scatter: Master Formula use karke numbers distribute karna
#     for num in arr:
#         # Step 1: Ratio nikalo (0.0 se 1.0)
#         ratio = (num - min_val) / (max_val - min_val)
        
#         # Step 2: Index nikalo aur decimals hata do int() use karke
#         index = int(ratio * (n - 1))
        
#         # Number ko uski bucket mein daal do
#         buckets[index].append(num)

#     print(f"Buckets distribution: {buckets}")

#     # D. Gather aur Sort
#     sorted_arr = []
#     for bucket in buckets:
#         # Agar bucket khali nahi hai
#         if len(bucket) > 0:
#             # Apna custom sort lagao
#             sorted_bucket = custom_insertion_sort(bucket)
            
#             # Ek ek element nikaal kar final list mein daalo (no .extend() used)
#             for item in sorted_bucket:
#                 sorted_arr.append(item)

#     return sorted_arr

# # ================================
# # TEST KARKE DEKHTE HAIN
# # ================================
# nums = [32, 10, 45, 23, 16, 50, 11]

# print("Original Array:", nums)
# print("-" * 40)
# final_result = ultimate_bucket_sort(nums)
# print("-" * 40)
# print("Sorted Array:", final_result)


arr  = [42, 35, 45, 38, 35, 48, 30]
n = len(arr)#num of buckets aaagyi 7 bucks
bucket = [[] for _ in range(n)]
mini = min(arr)
maxi = max(arr)
denominator = maxi-mini

# now have to palace in bucket 
for num in arr :#comes 42 rfist
    ratio = (num-mini)/denominator
    index= int(ratio*(n-1))#n-1 as bucket starta from 0 to 6 total 7 
    bucket[index].append(num)
# this will have all the bucket scontnaintg numebrs in them 
print(f"thsi is the arr having unsorted nusm  : {bucket}")
ans = []
# now just hace ot sort them
for bucks in bucket:
    bucks.sort()
    ans.extend(bucks)
print(ans)