preProcess = input().split()
input_ = []
for item in preProcess:
  if item[0] != "N":
    input_.append(int(item))
  else:
    input_.append(None)

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

from collections import deque

to_do_list = deque()

root = Node(input_[0])
input_.pop(0)

to_do_list.append(root)

def getNeighbors(queue):
    left_value = queue.pop(0)
    right_value = queue.pop(0)
    
    leftNode = None
    if left_value != None:
        leftNode = Node(left_value)
        
    rightNode = None
    if right_value != None:
        rightNode = Node(right_value)
        
    
    return leftNode, rightNode

while True:
    if len(to_do_list) == 0:
        break
    
    if len(input_) == 0:
        break
    
    current_node = to_do_list.popleft()
    
    leftNode, rightNode = getNeighbors(input_)

    if current_node != None:
        current_node.left = leftNode
        current_node.right = rightNode
    
    to_do_list.append(leftNode)
    to_do_list.append(rightNode)
    

def printTreePreOrder(root):
    if root == None:
        return
    
    #print(root.value)
    printTreePreOrder(root.left)
    printTreePreOrder(root.right)
    
printTreePreOrder(root)

path = []

def maxSum(root, rootValue):
    if root == None:
        path.append(rootValue)
        return 0
    
    root_value = root.value
    left_tree_max_value = maxSum(root.left, rootValue + " " + str(root.value))
    right_tree_max_value = maxSum(root.right,rootValue + " " + str(root.value))
    
    return max(root_value + left_tree_max_value,\
        root_value + right_tree_max_value)
        
root_value = ""
maxSum(root,root_value)
#print("Full path list", path)

max_path_sum = float("-inf")
max_sequence = ""

for item in path:
    path_sum = 0
    for element in item.split():
        path_sum = path_sum + int(element)
    if path_sum > max_path_sum:
        max_path_sum = path_sum
        max_sequence = item.split()
        
print(" ".join(max_sequence))
print(max_path_sum)
