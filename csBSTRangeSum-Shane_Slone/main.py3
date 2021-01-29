#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    total = 0
    def dft(n):
        nonlocal total
        if n is None:
            return
        if lower <= n.value <= upper:
            total += n.value
        dft(n.left)
        dft(n.right)
    dft(root)
    return total