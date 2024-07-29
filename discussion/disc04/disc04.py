def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)
    # def ways(i,j):
    #     if i == m and j == n:
    #         return 1
    #     elif i == m:
    #         return ways(i,j+1)
    #     elif j == n:
    #         return ways(i+1, j)
    #     else:
    #         return ways(i+1,j) +ways(i, j+1)
    # return ways(1,1)

# First approach this problem with a normal for loop
def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    count = 0
    output = []
    for i in s:
        if count % 2 == 0:
            output += [count * i]
        count = count + 1
    return output

# list comprehension
def even_weighted_comprehension(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_comprehension(x)
    [0, 6, 20]
    """
    return [ i * s[i] for i in range(len(s)) if i % 2 == 0]



def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == label(t):  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        "*** YOUR CODE HERE ***"
        return any([has_path(b,p[1:]) for b in branches(t)])
        # def path_helper(index, t):
        #     if index == len(p):
        #         return True
        #     for ii in branches(t):
        #         if label(ii) == p[index]:
        #             return path_helper(index+1, ii)
        #     return False
        # return path_helper(1, t)


def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return [x]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
    return None


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the labels in leaves at each leaf of
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(i) for i in leaves])
    bs = [sprout_leaves(b, leaves) for b in branches(t)]
    return tree(label(t), bs)



def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])