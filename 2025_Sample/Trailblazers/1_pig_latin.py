letter = input()
suffix = ""
if letter[0].lower() in "aeiou":
  suffix = "-yay"
  result = letter + suffix
else:
  # string slicing
  result = letter[1:] + "-" + letter[0] + "ay"
print(result)
