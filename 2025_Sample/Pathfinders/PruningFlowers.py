flowers = input().split()
hashTable = {}
for flower in flowers:
  hashTable[flower] = True

for element in hashTable:
  print(element, end= " ")
