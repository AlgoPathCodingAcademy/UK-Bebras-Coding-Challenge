numbers = input().split()

#Convert string to integer first
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

saving_target = 1000
total = 0
# Note, the inital value is 1 not 0
days = 1
for number in numbers:
  dailySpend = 20
  dailyEarn = number
  total = total + dailyEarn - dailySpend
  if total <= saving_target:
    days = days + 1
  else:
    break
  
print(days)

