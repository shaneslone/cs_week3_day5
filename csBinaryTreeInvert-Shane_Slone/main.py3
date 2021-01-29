#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    def inner(n):
        if n is None:
            return
        temp = n.left
        n.left = n.right
        n.right = temp
        inner(n.left)
        inner(n.right)
    inner(root)
    return root
  
