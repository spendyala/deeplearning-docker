# Helper class for doubly-linked list
class Node:
  def __init__(self, key, val):
    self.next = None
    self.prev = None
    self.key = key
    self.val = val

class LRUCache:
  def __init__(self, n):
    self.n = n
    self.count = 0
    self.nodes = {}
    self.start = None
    self.end = None

  def get(self, key):
    # Get node for key if it exists
    node = self.nodes.get(key)
    if not node:
      return None

    # Move this node to front of list
    self.move_to_front(node)

    return node.val

  def set(self, key, val):
    node = self.nodes.get(key)

    if node:
      # Update existing node and move to front
      node.val = val
      self.move_to_front(node)
      return

    if self.count == self.n:
      # No space, so remove last item
      if self.end:
        del self.nodes[self.end.key]
        self.remove(self.end)
    else:
      self.count += 1

    # Finally create and insert the new node
    node = Node(key, val)
    self.insert(node)
    self.nodes[key] = node

  # Private helpers
  def insert(self, node):
    if not self.end:
      self.end = node
    if self.start:
      node.next = self.start
      self.start.prev = node
    self.start = node

  def remove(self, node):
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    if self.start == node:
      self.start = node.next
    if self.end == node:
      self.end = node.prev

  def move_to_front(self, node):
    # Remove node and re-insert at head
    self.remove(node)
    self.insert(node)
