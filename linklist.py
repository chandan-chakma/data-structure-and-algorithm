class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        # print(self.value,self.next)

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_beggining(self,value):
        new_node=Node(value)
        
        new_node.next=self.head
        self.head=new_node

    def insert_end(self,value):
        new_node= Node(value)
        # print("new node", new_node)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        # print("current is", current)
        while current.next is not None:
            current=current.next
            print("current",current)
        current.next=new_node
        # print("cur",current)



    def display(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next

        # print("None")

    def delete_beginig(self):
        if self.head is None:
            return
        self.head=self.head.next

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        previous= None
        current=self.head
        while current.next is not None:
            previous=current
            current=current.next
        previous.next=None


my_list=LinkedList()
# my_list.insert_beggining(5)
# # print(my_list)
# my_list.display()
# my_list.insert_beggining(10)
# my_list.display()
# my_list.insert_end(30)
# my_list.display()

my_list.insert_beggining(5)

my_list.delete_end()
my_list.display()