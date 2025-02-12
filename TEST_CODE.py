##### Global color variables #####
from colorama import Fore
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''
##################################

def result(flag):
  if flag:
    return f"{G}PASSED{W}"
  
  return f"{R}FAILED{W}"

def test_sequence(SLL, corr_sequ):
  try:
    walk = SLL.head
    for el in corr_sequ:
      if el != walk.value:
        return False
      
      walk = walk.next
    return True

  except:
    return False

def TEST_new_sll(SLL):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: New SLL Creation{W}\n")

    test = SLL.head == None
    print(f"New SLL head pointer is set to None: {result(test)}")

    test = SLL.tail == None
    print(f"New SLL tail pointer is set to None: {result(test)}")

    sz = SLL._SinglyLinkedList__size
    print(f"New SLL size attribute is private: {result(True)}")

    test = sz == 0
    print(f"Size of new SLL is zero: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_singly_node(SLL):
  print("~" * 50)
  print(f"{P}TEST CATEGORY: The SinglyNode class{W}\n")

  try:
    node1 = SLL().SinglyNode("A")
    print(f"{B}A temporary test node was created: {node1}{W}\n")
    print(f"SinglyNode class is nested within SinglyLinkedList: {result(True)}")

    test = node1.value == "A"
    print(f"SinglyNode value is set properly: {result(test)}")

    test = node1.next == None
    print(f"New SinglyNode next is set to None: {result(test)}\n")

    try:
      node1.set_next("B")
      print(f"SinglyNode next must be of type SinglyNode: {result(False)}")
    except:
      print(f"SinglyNode next must be of type SinglyNode: {result(True)}")

    node2 = SLL().SinglyNode("B")
    node1.set_next(node2)
    test = node1.next == node2 and node1.next.value == "B"
    print(f"SinglyNode set_next works correctly: {result(test)}")

  except:
    print(f"SinglyNode class is nested within SinglyLinkedList: {result(False)}")

  print("~" * 50, "\n\n")

def TEST_head_insert(SLL, class_ref):
  print("~" * 50)
  print(f"{P}TEST CATEGORY: The SinglyLinkedList head_insert{W}\n")

  temp_node = class_ref().SinglyNode("temp")

  SLL.head_insert("A")
  print(f"{B}A node was inserted: {SLL}{W}\n")

  test = type(SLL.head) == type(temp_node)
  print(f"SLL head_insert inserts new SinglyNode object: {result(test)}")

  test = SLL.head.value == "A" and SLL.tail.value == "A"
  print(f"Insert into an empty SLL updates head and tail pointers: {result(test)}")

  test = type(SLL.head) == type(SLL.tail) == type(temp_node)
  print(f"SLL head and tail pointers reference SinglyNode objects: {result(test)}")

  test = len(SLL) == 1
  print(f"SLL head_insert increases size attribute: {result(test)}")

  SLL.head_insert("B")
  print(f"\n{B}A second node was inserted: {SLL}{W}\n")

  test = SLL.head.value == "B" and SLL.tail.value == "A"
  print(f"SLL head_insert into non-empty list updates head pointer only: {result(test)}")

  test = SLL.head.next.value == "A" and SLL.tail.value == "A"
  print(f"Node connections between new head and next element are preserved: {result(test)}")

  for el in "CDE":
    SLL.head_insert(el)

  print(f"\n{B}Many new nodes were inserted: {SLL}{W}\n")

  test = test_sequence(SLL, "EDCBA")
  print(f"Node sequencing is correct, all pointers validated: {result(test)}")

  test = SLL.tail.value == "A" and SLL.tail.next == None
  print(f"SLL head_insert does not impact tail pointer: {result(test)}")

  test = len(SLL) == 5
  print(f"SLL head_insert properly impacts size attribute: {result(test)}")

  print("~" * 50, "\n\n")


def TEST_head_remove(SLL):
  print("~" * 50)
  print(f"{P}TEST CATEGORY: The SinglyLinkedList head_remove{W}\n")

  print(f"{B}Current state of SLL: {SLL}{W}\n")

  val = SLL.head_remove()
  print(f"{B}Head element |{val}| was removed: {SLL}{W}\n")

  test = type(val) == str
  print(f"SLL head_remove returns node value, not SinglyNode object: {result(test)}")

  test = val == "E"
  print(f"SLL head_remove returns correct value: {result(test)}")

  test = SLL.head.value == "D"
  print(f"SLL head_remove affects SLL head pointer: {result(test)}")

  test = len(SLL) == 4
  print(f"SLL head_remove decreases list size: {result(test)}")

  test = test_sequence(SLL, "DCBA")
  print(f"Node sequencing is correct, all pointers validated: {result(test)}")

  for i in range(4):
    SLL.head_remove()

  print(f"\n{B}SLL emptied with head_remove: {SLL}{W}\n")

  try:
    SLL.head_remove()
    print(f"Remove from empty SLL raises exception: {result(False)}")
  except:
    print(f"Remove from empty SLL raises exception: {result(True)}")

  test = len(SLL) == 0 and SLL.head == None and SLL.tail == None
  print(f"Emptied SLL resets head and tail pointers to None: {result(test)}")

  print("~" * 50, "\n\n")

def TEST_tail_insert(SLL, class_ref):
  print("~" * 50)
  print(f"{P}TEST CATEGORY: The SinglyLinkedList tail_insert{W}\n")

  print(f"{B}Current state of SLL: {SLL}{W}\n")

  temp_node = class_ref().SinglyNode("temp")

  SLL.tail_insert("A")
  print(f"{B}A node was inserted: {SLL}{W}\n")

  test = type(SLL.head) == type(temp_node)
  print(f"SLL tail_insert inserts new SinglyNode object: {result(test)}")

  test = SLL.head.value == "A" and SLL.tail.value == "A"
  print(f"Insert into an empty SLL updates head and tail pointers: {result(test)}")

  test = type(SLL.head) == type(SLL.tail) == type(temp_node)
  print(f"SLL head and tail pointers reference SinglyNode objects: {result(test)}")

  test = len(SLL) == 1
  print(f"SLL tail_insert increases size attribute: {result(test)}")

  SLL.tail_insert("B")
  print(f"\n{B}A second node was inserted: {SLL}{W}\n")

  test = SLL.tail.value == "B" and SLL.head.value == "A"
  print(f"SLL tail_insert into non-empty list updates tail pointer only: {result(test)}")

  test = SLL.head.next.value == "B" and SLL.tail.value == "B"
  print(f"Node connections between new head and next element are preserved: {result(test)}")

  for el in "CDE":
    SLL.tail_insert(el)

  print(f"\n{B}Many new nodes were inserted: {SLL}{W}\n")

  test = test_sequence(SLL, "ABCDE")
  print(f"Node sequencing is correct, all pointers validated: {result(test)}")

  test = SLL.tail.next == None
  print(f"SLL tail_insert does not set_next for new node: {result(test)}")

  test = len(SLL) == 5
  print(f"SLL tail_insert properly impacts size attribute: {result(test)}")

  print("~" * 50, "\n\n")


def TEST_head_tail_insert(SLL, class_ref):
  print("~" * 50)
  print(f"{P}TEST CATEGORY: The SinglyLinkedList head_insert & tail_insert{W}\n")
  
  temp_node = class_ref().SinglyNode("temp")
  for el in range(len(SLL)):
    SLL.head_remove()

  print(f"{B}SLL has been emptied: {SLL}{W}\n")

  for i, let in enumerate("ABCDEF"):
    if i % 2 == 0:
      SLL.head_insert(let)
    else:
      SLL.tail_insert(let)

  print(f"{B}Elements added to SLL with both insert methods: {SLL}{W}\n")

  test = type(SLL.head) == type(SLL.tail) == type(temp_node)
  print(f"SLL was populated with SinglyNode objects: {result(test)}")

  test = SLL.head.value == "E" and SLL.tail.value == "F"
  print(f"Head and tail values are correct: {result(test)}")

  test = len(SLL) == 6
  print(f"Insert methods affect size correctly: {result(test)}")

  test = SLL.tail.next == None
  print(f"Tail node has no next: {result(test)}")

  test = test_sequence(SLL, "ECABDF")
  print(f"Node sequencing is correct, all pointers validated: {result(test)}")

  print("~" * 50, "\n\n")

def TEST_docs(SLL, class_ref):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    print("SinglyNode Class Docstrings:\n")
    doc = class_ref.SinglyNode.set_next.__doc__
    if doc != None:
        print(f"{B}set_next() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_next() Documentation Missing{W}\n")

    doc = class_ref.SinglyNode.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")
    
    print("\n\nSinglyLinkedList Class Docstrings:\n")
    doc = SLL.head_insert.__doc__
    if doc != None:
        print(f"{B}head_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_insert() Documentation Missing{W}\n")

    doc = SLL.tail_insert.__doc__
    if doc != None:
        print(f"{B}tail_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}tail_insert() Documentation Missing{W}\n")

    doc = SLL.head_remove.__doc__
    if doc != None:
        print(f"{B}head_remove() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_remove() Documentation Missing{W}\n")

    doc = SLL._SinglyLinkedList__is_empty.__doc__
    if doc != None:
        print(f"{B}is_empty() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_empty() Documentation Missing{W}\n")

    doc = SLL.__len__.__doc__
    if doc != None:
        print(f"{B}len() Documentation:{W} {doc}\n")
    else:
        print(f"{R}len() Documentation Missing{W}\n")

    doc = SLL.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")