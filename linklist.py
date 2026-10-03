class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


my_list = LinkedList()
# print(my_list)

node1=Node(10)
print(node1)
my_list.head=node1
print(my_list)
node2=Node(20)
node1.next=node2
node3=Node(30)
node2.next=node3

print(my_list.head.value)