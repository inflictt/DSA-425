# # Easiest Huffman Coding

# chars = ['A', 'B', 'C', 'D']
# freq = [5, 9, 12, 13]

# data = list(zip(chars, freq))
# data.sort(key=lambda x: x[1])

# for i in range(len(data)):
#     char = data[i][0]
#     code = bin(i)[2:]
#     print(char, " = ", code)


freq = {
    'P': 10,
    'Y': 4,
    'Q': 22,
    'L': 19,
    'M': 6,
    'F': 8,
    'O': 31,
    'R': 40,
    'S': 30
}

char = list(freq.keys())
freq = list(freq.values())
data = list(zip(char, freq))
for i in range(len(data)):
    char = data[i][0]
    code = bin(i)[2:]
    print(f"char is {char} and code is {code}")
