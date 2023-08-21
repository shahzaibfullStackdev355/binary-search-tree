class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root,val):

    if root == None:
        # root = Node(val)
        return Node(val)
    
    if val < root.data:
        # left part me insert karna
        root.left = insert(root.left,val)
    else:
        # right part me insert karna
        root.right = insert(root.right,val)
    

    return root


def inOrderTraversal(root):
    if root == None:
        # print("-1", end=" ")
        return

    inOrderTraversal(root.left)
    print(root.data, end=" ")
    inOrderTraversal(root.right)




def searchNodeBST(root,key):

    if root == None:
        return False
    
    if key < root.data:
        print("root.left: ", root.left)
        return searchNodeBST(root.left,key)
    
    elif root.data == key:
        print(root.data)
        return True
    
    else:
        print("root.right: ", root.right.data)
        return searchNodeBST(root.right,key)
    




def deleteNodeBST(root,val):

    if val < root.data:
        root.left = deleteNodeBST(root.left,val)

    elif val > root.data:
        root.right = deleteNodeBST(root.right,val)

    else: #root.data == val

        # case 1
        if root.left == None and root.right == None:
            return None
        

        # case 2
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        
        inOrderSuccess = inOrderSuccessorBST(root.right)
        root.data = inOrderSuccess.data
        deleteNodeBST(root.right, inOrderSuccess.data)

    return root

def inOrderSuccessorBST(root):
    
    while root.left != None:
        root = root.left


    return root











# values = [5,1,3,4,2,7]
# values = [4,2,5,1,3,6]
values = [8,5,3,1,4,6,10,11,14]

root = None
for i in range(len(values)):
    root = insert(root,values[i])




# def treeCreation(root):

#     rootNode = int(input("Enter Data: "))

#     data = Node(rootNode)

#     while data != -1:
#         insert(root,data)
        

# root = None
# tree = treeCreation(root)





# inOrderTraversal(root)

searchNode = searchNodeBST(root,10)

if searchNode:
    print("true")
else: 
    print("false")