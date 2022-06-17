class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#The function below is used to take input for the linked list    
def take_input():
    li = [int(i) for i in input().split()]
    head = None
    tail = None
    for i in li:
        if i == -1:
            break
        newNode = Node(i)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head 

#This function below returns the length of the linked list
def length(head) :
    #Your code goes here
    count = 0
    while head is not None:
        count +=1
        head = head.next
    return count
    
# This function below is used to delete a position given from the linked list   
def deleteNode(head, pos) :
    # Write your code here.
    if pos<0 or pos>=length(head):
        #print(length(head))
        return head
    else:
        prev = None
        curr = head
        count = 0
        if length(head) <=1:
            head = None
            return head
        else:
            while count <pos:
                prev = curr
                curr = curr.next
                count +=1
            if prev is not None:
                if curr is not None:
                    prev.next = curr.next
                else:
                    prev.next = None
            else:
                if head is not None:
                    head = head.next
                else:
                    head = None
            return head
            
# The function below is used to remove duplicates from the linked list           
def removeDuplicates(head) :
    #Your code goes here
    temp = head
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
    return head

# The function below is used to return the reverse linked list using recursion
def reverse(head):
    # Write your code here
    if head is None or head.next is None:
        return head
    smallhead = reverse(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

# The function below can be used to find the first occurence of a value in a linked list
def findNodeRec(head, n) :
	#Your code goes here
    count = 0
    while head is not None:
        if head.data == n:
            return count
        count +=1
        head = head.next
    return -1

# The below function is used to print the linked list   
def printll(head):
    while head is not None:
        print(head.data,end="->")
        head = head.next
    print("None")

# The below function is used to swap two nodes with given positions i.e 'i' and 'j'
def swapNodes(head, i, j) :
	#Your code goes here
    head_ref = head
 
    # Nothing to do if x and y are same
    if (i == j) or head is None:
        return head
 
    a = None
    b = None
    counta = 0
    countb = 0
    # search for x and y in the linked list
    # and store their pointer in a and b
    while (head_ref != None):
 
        if (counta == i):
            a = head_ref
 
        elif (countb == j):
            b = head_ref
 
        counta +=1
        countb +=1
        head_ref = ((head_ref).next)
    #print(a,b)
    # if we have found both a and b
    # in the linked list swap current
    # pointer and next pointer of these
    if (a != None and b != None):
        temp = a.data
        a.data = b.data
        b.data = temp
         
    return head
# The below function is the bubblesort in Linked list
def bubbleSort(head) :
	#Your code goes here
    temp = head
    curr = head
    n = length(head)
    for i in range(n):        
        while curr.next is not None:
            if curr.data > curr.next.data:
                temp1 = curr.next.data
                curr.next.data = curr.data
                curr.data = temp1
            curr = curr.next
        curr = temp
        n = n+1
        #return head
    #temp = temp.next
    return head
   
head = take_input()     
printll(head)      
