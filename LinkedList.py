class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4=Node("Thur")
e5=Node("Fri")
e6=Node("Sat")
e7=Node("sun")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
list.listprint()