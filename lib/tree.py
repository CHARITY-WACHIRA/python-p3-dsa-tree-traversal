class Tree:

  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    """Traverse the tree using depth-first search and return the node with the given id.
    If no node is found with the given id, return None."""
    stack =[self.root]

    while stack:
      node=stack.pop()

      if node.get('id')==id:
        return node
      
      stack.extend (reversed(node.get('children',[])))

    return None

