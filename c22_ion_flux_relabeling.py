def parent(h, node):
    """
    Find the parent of the given node.

    :param h: the height of the tree
    :param node: the node whose parent we seek
    :return: the parent of the given node
    """
    start = 1
    root = pow(2, h) - 1

    # return -1 if node is a root node
    if node == root:
        return -1

    # otherwise, let's initialize end to be same as root
    end = root

    # Find the given node
    while node > 0:
        end = end - 1

        # Find the middle node of the tree because at every level, the tree parent is divided into two halves
        middle_node = start + (end - start) // 2

        # if the node is found then return the parent;
        # the child nodes of every node is either (node / 2) or (node-1)
        if middle_node == node or end == node:
            return end + 1

        # if the node to be found is greater than the mid then search the left subtree
        elif node < middle_node:
            end = middle_node
        # else search the right subtree
        else:
            start = middle_node


def solution(h, q):
    """
    :param h: the height of the perfect tree of converters
    :param q: a list of positive integers representing different flux converters
    :return: a list of integers p where each element in p is the label of the converter that sits on top of the
            respective converter in q, or -1 if there is no such converter
            
    """
    max_nodes = pow(2, h + 1) - 1
    root = pow(2, h) - 1
    num_flux_converters = len(q)
    no_such_converter = -1

    print("tree height = {}; nodes = {}; root node = {}; len(q)={}".format(h, max_nodes, root, num_flux_converters))

    # The domain of h is 1 <= h <= 30
    if h < 1 or h > 30:
        return [no_such_converter]

    # There can't be more flux converters than there are nodes in the tree
    if num_flux_converters > max_nodes:
        return [no_such_converter]

    # The list q contains at least one but no more than 10000 distinct integers
    converter_size_limit = 10000
    if num_flux_converters < 1 or num_flux_converters > converter_size_limit:
        return [no_such_converter]

    p = []

    for flux_converter in q:

        # p cannot have more than 10000 converters
        if len(p) >= converter_size_limit:
            break

        # No flux converter can be bigger than the max node value in the tree
        if flux_converter <= max_nodes:

            # Each node with value n is a parent for (n-1)/2 on the LEFT and (n-1) on the RIGHT.
            parent_node = parent(h, flux_converter)

            # p contains distinct integers, i.e., a flux converter can be present at most once
            if parent_node not in p:
                p.append(parent_node)

    # The list p contains at least one converter
    if len(p) < 1:
        p = [no_such_converter]

    return p

#h = 3
#q = [1,4,7]
#print(solution(h,q))