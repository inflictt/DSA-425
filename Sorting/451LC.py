# 451. Sort Characters By Frequency
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together
# nlogn is tc
s = "Aabb"

# bigAlpha = {}

# new_s = ""
# for ch in s:
#     bigAlpha[ch] = bigAlpha.get(ch, 0)+1

# sorted_dict = dict(sorted(bigAlpha.items(), key=lambda x: x[1], reverse=True))

# print(bigAlpha)
# print(sorted_dict)
# for key, val in sorted_dict.items():
#     new_s += key*val
# print(new_s)

# opitmal
n = len(s)
hashmap = {}
for ch in s:
    hashmap[ch] = hashmap.get(ch, 0)+1
# hashmap created with values now distribute these into buckets
# AtoZ is 65 to 90 and a to z is 67 to 122 = 52buckets
bucket = [[] for _ in range(n+1)]
for key, val in hashmap.items():
    bucket[val].append(key)
# to is se ye hoga ki jitni value hoga utni us mai key mtlb char add ho jaeyga aur highesrt value wala piche se sbse pehele toh reverse loop se add krke print dengey
ans = ""
for freq in reversed(range(n+1)):  # piche sbse jayda freq h
    for ch in bucket[freq]:  # har ek bucket iterate krengey
        ans += ch*freq
print(ans)
