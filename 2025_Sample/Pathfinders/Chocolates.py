chocolates = input().split()
for i in range(len(chocolates)):
  chocolates[i] = int(chocolates[i])

sorted_chocolates = sorted(chocolates)
total = 0
for i in range(0,len(sorted_chocolates),2):
  total = total + sorted_chocolates[i]

print(total)
