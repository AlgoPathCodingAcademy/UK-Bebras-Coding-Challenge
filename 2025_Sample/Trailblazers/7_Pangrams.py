# HashTable

input_list = input().split()
hashTable = {}
ascii_value_a = ord("a")
for i in range(26):
  hashTable[chr(ascii_value_a+i)] = 0

for word in input_list:
  word = word.lower()
  for letter in word:
    if letter in hashTable:
      hashTable[letter] = hashTable[letter] + 1

isPangram = True
for key in hashTable:
  if hashTable[key] == 0:
    isPangram = False
    break

if isPangram:
  print("Pangram")
else:
  print("Not a pangram")
