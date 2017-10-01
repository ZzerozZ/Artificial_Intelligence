
def depth_first_search(root, value):
    if root.name == value:
        return 1

    if root.is_leaf == True:
        return 0

    for child in root.children:
        if depth_first_search(child, value) == 1:
            return 1
    return 0


def breadth_first_search(root, value):
    if root.name == value:
        return 1

    for child in root.children:
        if child.name == value:
            return 1

    for child in root.children:
        for nephew in child.children:
            if breadth_first_search(nephew, value) == 1:
                return 1
    return 0

