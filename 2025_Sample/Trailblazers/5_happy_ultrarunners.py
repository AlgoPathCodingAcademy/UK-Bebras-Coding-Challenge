# GCSE question
def isConsecutiveSequence(lst):
  isBigger = True
  for index in range(len(lst)-1):
      if lst[index+1] <= lst[index]:
        isBigger = False
        break
  return isBigger

nums = int(input())
result = 0
for i in range(nums):
  input_list = [int(item) for item in input().split()]
  if isConsecutiveSequence(input_list):
    result = result + 1
print(result)
