isValid = True
input_str = input().split(".")
for item in input_str:
  for letter in item:
    if letter not in "0123456789":
      isValid = False
      break
  if not isValid:
    break

info = []

if isValid:
  info = [int(item) for item in input_str]

if len(info) != 4:
  isValid = False

if isValid:
  for item in info:
    if item < 0 or item > 255:
      isValid = False
      break
  if isValid:
    print("Valid IP address")
  else:
    print("Invalid IP address")
else:
  print("Invalid IP address")

