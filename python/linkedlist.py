class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def appendnode(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head=newnode
            return 
        currentnode=self.head
        while currentnode.next:
            currentnode=currentnode.next
        currentnode.next=newnode

    def display(self):
        currentnode=self.head
        while currentnode:
            print(currentnode.data, end="->")
            currentnode=currentnode.next
    
    def insert(self,data):
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        currentdata=self.head
        while currentdata !=None and currentdata.data<data:
            prev=currentdata
            currentdata=currentdata.next
        newnode=Node(data)
        prev.next=newnode
        newnode.next=currentdata

    def delete(self,data):
        currentnode=self.head
        # if currentnode.data==data:
        #     self.head.next=self.head
        #     return
        # currentnode=self.head
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        
        while currentnode.data!=data:
            prev=currentnode
            currentnode=currentnode.next
        prev.next=currentnode.next
        self.head=dummy.next

        

lst=Linkedlist()
lst.appendnode(10)
lst.appendnode(20)
lst.appendnode(30)
lst.insert(35)
lst.delete(10)
lst.display()