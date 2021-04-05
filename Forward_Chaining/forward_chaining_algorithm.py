# key = parent, value = child
parent_table = {
    'a': {'z', 'r'},
    'z': {'x', 'y'},
    #    'w' : {'u', 'v'},
    'r': {'p', 'q'}
}

# key = child, value = parent
child_table = {
    'u': {'w'},
    'v': {'w'}
}

grand_parent_table = {}


def is_parent(x, y):  # x is a parent of y
    if x not in parent_table.keys():
        parent_table[x] = set()
    # check in existing knowledge base
    for child in parent_table[x]:
        if child == y:
            return True
    # add data to knowledge base
    for child, parent_list in child_table.items():
        for parent in parent_list:
            if parent not in parent_table.keys():
                parent_table[keys] = set()
            parent_table[parent].add(child)
            if child == y and parent == x:
                return True
    return False


def is_child(x, y):  # x is a child of y
    if x not in child_table.keys():
        child_table[x] = set()
    # check in existing knowledge base
    if y in child_table[x]:
        return True
    for parent, child_list in parent_table.items():
        for child in child_list:
            if child not in child_table.keys():
                child_table[child] = set()
            child_table[child].add(parent)
            if child == x and parent == y:
                return True
    return False


def is_grand_parent(x, y):  # x is a grand parent of y
    if x not in grand_parent_table.keys():
        grand_parent_table[x] = set()
    if y in grand_parent_table[x]:
        return True
    for child in parent_table[x]:
        for child_of_child in parent_table[child]:
            grand_parent_table[x].add(child_of_child)
            if child_of_child == y:
                return True
    return False


print(f"w is parent of u -> {is_parent('w', 'u')}")
print(f"u is parent of w -> {is_parent('u', 'w')}")
print(f"y is a child of z -> {is_child('y', 'z')}")
print(f"y is a child of w -> {is_child('y', 'w')}")
print(f"a is grand parent of q -> {is_grand_parent('a', 'q')}")
print(f"a is grand parent of v -> {is_grand_parent('a', 'v')}")

print("Final knowledge base:-")
print("grand parent:")
print(grand_parent_table)
print("parent")
print(parent_table)
print("child")
print(child_table)
