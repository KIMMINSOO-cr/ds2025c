class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = "HS"

node2 = TreeNode()
node2.data = "SL"
node1.left = node2

node3 = TreeNode()
node3.data = "ha"
node1.right = node3

node4 = TreeNode()
node4.data = "zz"
node2.left = node4

node5 = TreeNode()
node5.data = "rr"
node2.right = node5

node6 = TreeNode()
node6.data = "aa"
node3.left = node6

print(node4.data)
print(node1.left.right.data)
