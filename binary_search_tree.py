class BSTNode:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
     
def insert(root, val):
  """ Time complexity - O(h) since it inserts at leaf node
      space complexity - O(h) , h - height of the tree
  """
  if root is None:
     root = BSTNode(val) 
  elif val < root.data:
     root.left = insert(root.left, val)
  elif val > root.data:
     root.right = insert(root.right, val)
  elif val == root.data:
    print(f"Node with given data already exists. Can't insert duplicates. val={val}, root.data {root.data}")
  return root

def preorder(root: Optional[BSTNode]):
  """ Time complexity - O(n) since it visits each node
      space complexity - O(h) , h - height of the tree
  """
  if root is not None:
    print(root.data)
    preorder(root.left)
    preorder(root.right)
  return

def inorder(root: Optional[BSTNode]):
  """ Time complexity - O(n) since it visits each node
      space complexity - O(h) , h - height of the tree
  """
  if root is not None:
    inorder(root.left)
    print(root.data)
    inorder(root.right)
  return

def postorder(root: Optional[BSTNode]):
  """ Time complexity - O(n) since it visits each node
      space complexity - O(h) , h - height of the tree
  """
  if root is not None:
    postorder(root.left)
    postorder(root.right)
    print(root.data)
  return

if __name__ == "__main__":
  treenode = BSTNode(5)
  keys = [4,3,8,7,10]
  for k in keys:
    _ = insert(treenode, k)
  print("\nInorder traversal")
  inorder(treenode)
  print("\nPreorder traversal")
  preorder(treenode)
  print("\nPostorder traversal")
  postorder(treenode)
  
