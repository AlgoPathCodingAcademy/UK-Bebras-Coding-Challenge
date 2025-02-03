maze = []
for i in range(3):
  row_line = [int(item) for item in input().split()]
  maze.append(row_line)


def is_diag_sum_match(maze):
  direction = (1,1)
  result_right_down = 0
  new_row = 0
  new_column = 0
  while True:
    #print("new_row",new_row)
    #print("new_column",new_column)
    
    if new_row == len(maze) or new_column == len(maze[0]):
        break
    result_right_down = result_right_down + maze[new_row][new_column]
    new_row = new_row + direction[0]
    new_column = new_column + direction[1]
    
  #print(result_right_down)

  direction = (1,-1)
  result_left_down = 0
  new_row = 0
  new_column = len(maze[0]) - 1
  while True:
    if new_row == len(maze) or new_column == len(maze[0]):
        break
    result_left_down = result_left_down + maze[new_row][new_column]
    new_row = new_row + direction[0]
    new_column = new_column + direction[1]
    
  #print(result_left_down)

  if result_left_down == result_right_down:
     return (True,result_left_down)
  else:
     return (False,None)

def is_row_sum_match(maze):
  save_list = []
  for row in range(len(maze)):
    line_total = 0

    for column in range(len(maze[0])):
      line_total = line_total + maze[row][column]
      
    save_list.append(line_total)

  isSame = True
  for index in range(len(save_list)-1):
     if save_list[index] != save_list[index+1]:
       isSame = False

  if isSame:
     return (True,save_list[0])
  else:
     return (False,None)

def is_colum_sum_match(maze):
   save_list = []
   for column in range(len(maze[0])):
     total_column = 0
     for row in range(len(maze)):
       total_column = total_column + maze[row][column]
     save_list.append(total_column)

   isSame = True
   for index in range(len(save_list)-1):
     if save_list[index] != save_list[index+1]:
       isSame = False

   if isSame:
     return (True,save_list[0])
   else:
     return (False,None)

colum_result = is_colum_sum_match(maze)
diag_result = is_diag_sum_match(maze)
row_result = is_row_sum_match(maze)
#print(colum_result)
#print(diag_result)
#print(row_result)
if colum_result[0] and diag_result[0] and row_result[0]:
  if colum_result[1] == 15 and \
    diag_result[1] == 15 and \
    row_result[1] == 15:
    print("magic")
else:
    print("muggle")
