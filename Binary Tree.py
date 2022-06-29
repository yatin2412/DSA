# The complete Binary tree concepts and questions and some
#imp questions in the modules as well
#Go through the module surely

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    # Your code goes here
    #This with the help of queue will print the data levelwise
    if root is None:
        return None
    q = deque()
    q.append(root)
    while len(q) != 0:
        current = q.popleft()
        if current.left is not None:
            print(current.data,end = "")
            print(":L:",end = "")
            print(current.left.data,end = ",")
            q.append(current.left)
        else:
            print(current.data,end = "")
            print(":L:",end = "")
            print("-1",end = ",")
            
        if current.right is not None:
            print("R:",end = "")
            print(current.right.data,end = "")
            q.append(current.right)
            print()
        else:
            
            print("R:",end = "")
            print("-1",end = "")
            print()

    
def getSum(root):
	#Your code goes here   
    if (root == None):
        return 0
    return (root.data + getSum(root.left) + getSum(root.right))
    
    
def preOrder(root):
	# Your code goes here
    if root == None:
        return
    print(root.data,end = " ")
    preOrder(root.left)
    preOrder(root.right)


def countNodesGreaterThanX(root, x) :
	#Your code goes here
    if root is None:
        return 0
    count = 0
    count += countNodesGreaterThanX(root.left, x)
    count += countNodesGreaterThanX(root.right, x)
    if root.data>x:
        count+=1
    return count


def height(root) :
	#Your code goes here
    if root == None:
        return 0
    left_height = 0
    right_height = 0
    left_height = height(root.left)
    right_height = height(root.right)
    left_height +=1
    right_height+=1
    return max(left_height,right_height)


def isNodePresent(root, x):
    # Write your code here.
    if root is None:
        return 0
    if root.data == x:
        return True
        
    return isNodePresent(root.left,x)
    return isNodePresent(root.right,x)


def printNodesWithoutSibling(root) :
	# Your code goes here
    if root is None:
        return 0
    if root.left is not None and root.right is None:
        print(root.left.data,end=" ")
    if root.left is None and root.right is not None:
        print(root.right.data,end = " ")
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)


#To check if the binary tree is balanced or not:-
# 1. Take the left height and the right height using height function
# 2. if left height - right height > 1: then false else true


 

def buildTree(preOrder, inOrder, n) :
	#Your code goes here
    # Easy concept just go through the video once
    if len(preOrder) == 0:
        return None
    rootdata = preOrder[0]
    root = BinaryTreeNode(rootdata)
    for i in range(len(inOrder)):
        if inOrder[i] == rootdata:
            index = i
    left_inorder = inOrder[0:index]
    right_inorder = inOrder[index+1:]
    
    length1 = len(left_inorder)
    
    left_preorder = preOrder[1:length1+1]
    right_preorder = preOrder[length1+1:]
    
    left_child = buildTree(left_preorder,left_inorder,n)
    right_child = buildTree(right_preorder,right_inorder,n)
    
    root.left = left_child
    root.right = right_child
    
    return root



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root



# Main
root = takeInput()
print(getSum(root))