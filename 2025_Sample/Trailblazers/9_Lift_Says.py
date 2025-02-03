# 2D List
sequences = input().split(",")
input_info = []
for index in range(len(sequences)):
  item = sequences[index]
  elements = item.split()
  input_info.append([int(item) for item in elements])

result = 0
for index in range(len(input_info)):
    result = result - input_info[index][0]
    result = result + input_info[index][1]
    
print(result)
