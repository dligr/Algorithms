
def walk_around_prefix(root, edges, result, visited=[]):
    visited.append(root)
    result.append(root)
    for i in edges:
        if (i[0] == root and i[1] not in visited):
            walk_around_prefix(i[1], edges, result, visited)
        elif (i[1] == root and i[0] not in visited):
            walk_around_prefix(i[0], edges, result, visited)
    return result

def walk_around_postfix(root, edges, result, visited=[]):
    visited.append(root)
    for i in edges:
        if i[0] == root and i[1] not in visited:
            walk_around_postfix(i[1], edges, result, visited)
        elif i[1] == root and i[0] not in visited:
            walk_around_postfix(i[0], edges, result, visited)
    result.append(root)
    return result