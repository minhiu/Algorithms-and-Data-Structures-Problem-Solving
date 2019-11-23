### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  def insert(self, data, index):
    if index == 0:
      new_node = LinkedNode(data)
      new_node.next = self.head
      self.head = new_node
    
    elif index == self.getCount():
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
    
    else:
      temp = self.head.next
      tail_temp = self.head
      
      i = 1
      while (i < index):
        temp = temp.next
        tail_temp = tail_temp.next
        i += 1
      
      new_node = LinkedNode(data)
      new_node.next = temp
      tail_temp.next = new_node
  
  def getCount(self):
    temp_node = self.head
    count = 0
    
    while (temp_node):
      count += 1
      temp_node = temp_node.next
    
    return count