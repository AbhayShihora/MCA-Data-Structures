#Design a Chess Player Ranking System using a Binary Search Tree (BST) where players are stored according 
# to their ELO rating. The system should support insertion of new players, searching a player by ELO, and 
# displaying players in ascending order of ELO.


#BST
class Node():
    def __init__(self,name,elo):
        self.name=name;
        self.elo=elo
        self.left=None
        self.right=None

def insert(root,name,elo):
    if root is None:
        return Node(name,elo)
    elif elo < root.elo:
        root.left=insert(root.left,name,elo)
    else:
        root.right=insert(root.right,name,elo)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.name," - ",root.elo)
        inorder(root.right)

root=None
root=insert(root,"Abhay",1800)
root=insert(root,"Smit",1700)
root=insert(root,"Ayush",1900)
root=insert(root,"Mahesh",1750)
root=insert(root,"Ravi",1800)

inorder(root)
