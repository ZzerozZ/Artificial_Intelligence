from anytree import Node
from Uninformed_Search import breadth_first_search


root = Node(100)
left = Node(29, parent=root)
right = Node(209, parent=root)

left2 = Node(12, parent=left)
right2 = Node(600, parent=right)

print breadth_first_search(root, 29)
