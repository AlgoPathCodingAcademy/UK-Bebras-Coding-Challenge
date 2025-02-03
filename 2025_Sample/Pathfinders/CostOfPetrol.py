litres = input().split()
total = 0
for litre in litres:
  total = total + int(litre)

print(int(total*0.0024))
