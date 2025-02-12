class SinglyLinkedList:

  class SinglyNode:
    def __init__(self, value=None):
      self.value = value
      self.next = None
    
    def set_next(self, node):
      """Sets next node reference"""
      if type(node) == type(self):
        self.next = node
      else:
        raise Exception("Wrong type")

    def __str__(self):
      """To string for singly node"""
      return f"|{self.value}|"


  def __init__(self):
    self.head = None
    self.tail = None
    self.__size = 0

  def head_insert(self, value):
    """Inserts the new node at the head of list"""
    new_node = self.SinglyNode(value)
    if self.__is_empty():
      self.head = self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node
    self.__size += 1

  def tail_insert(self, value):
    """Inserts new node at the tail of the list"""
    new_node = self.SinglyNode(value)
    if self.__is_empty():
      self.head = self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    self.__size += 1
  
  def head_remove(self):
    """Removes the node from the head of the list and returns it"""
    if self.__is_empty():
      raise Exception("Cannot remove from empty list")
    removed_value = self.head.value
    self.head = self.head.next
    if self.head is None:
      self.tail = None
    self.__size -= 1
    return removed_value

  def __len__(self):
    """Returns the size of the list"""
    return self.__size
    
  def __is_empty(self):
    """Checks if the list is empty"""
    return self.__size == 0

  def __str__(self):
      """To string for Singly linked list"""
      out = "HEAD > "

      walk = self.head
      for i in range(self.__size):
          out += f"{walk} "
          walk = walk.next
          if walk != None:
              out += "-> "

      out += "< TAIL"
      return out

  
  


