# list split and 2d list
total = 0
input_lst = input().split(",")
for item in input_lst:
  item_list = item.split()
  up = int(item_list[0])
  down = int(item_list[1])
  total = total + up - down
print(total)
