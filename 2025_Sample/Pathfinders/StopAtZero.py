while True:
  nums = int(input())
  if nums <= 0:
    break
  # simpler version
  # print(nums*"-")
  symbol = ""
  for i in range(nums):
    symbol = symbol + "-"
  print(symbol)
