class Node :
    def __init__(self , data ):
        self.data = data 
        self.nref = None 
        self.pref = None 
        
class DoubleLinkedList:
    def __init__ (self):
        self.head = None 
        
    def print_ll ( self ): 
        if self.head is None: 
            print("Liniked list is empty")
        else:
            n = self.head 
            while n is not None: 
                print(n.data)
                n = n.nref 
        
    def print_ll_rev ( self ): 
        if self.head is None: 
            print("Liniked list is empty")
        else:
            # go lo last node 
            
            n = self.head 
            while n.nref is not None: 
                n = n.nref 
                
            while n is not None:
                print(n.data)
                n = n.pref 
                
                
    def insert_empty (self , data ):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            
    def insert_first(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head 
            self.head.pref = new_node
            self.head = new_node
            
    def add_end(self ,data ):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref 
                
            n.nref = new_node 
            new_node.pref = n 
            
        
    def add_after(self, data , x ):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head 
            while n is not None:
                if x == n.data:
                    break 
                else:
                    n = n.nref 
                    
            if n is None:
                print("Given node is not present")
            else:
               new_Node = Node(data) 
               new_Node.nref = n.nref 
               new_Node.pref = n 
               if n.nref is not None:
                   n.nref.pref = new_Node
               n.nref = new_Node
                    
            
    def add_before(self, data , x ):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head 
            while n is not None:
                if x == n.data:
                    break 
                else:
                    n = n.nref 
                    
            if n is None:
                print("Given node is not present")
            else:
               new_Node = Node(data) 
               new_Node.nref = n 
               new_Node.pref = n.pref
               
               if n.pref is not None:
                   n.pref.nref = new_Node
               else:
                   self.head = new_Node
                   
               n.pref = new_Node
                    


ll = DoubleLinkedList()
ll.add_end(3)
ll.add_before(2,3)
ll.add_after(4,3)
ll.insert_first(1)
ll.print_ll()