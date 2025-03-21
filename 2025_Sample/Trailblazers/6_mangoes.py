# Sum and corner case
days = int(input())
result = 0
left = 0
new = 0
total_new = 0
for day in range(days):
  amount = [int(item) for item in input().split()]

  # corner case
  new = amount[1] - left
  if new < 0 :
    new = 0
  left = left + amount[0] - amount[1]
  total_new = total_new + new

print(total_new)
