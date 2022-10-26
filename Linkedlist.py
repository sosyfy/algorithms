# linked list 

class Node :
    def __init__(self, data ):
        self.data = data
        self.ref = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def print_ll ( self ): 
        if self.head is None: 
            print("Liniked list is none")
        else:
            n = self.head 
            while n is not None: 
                print(n.data)
                n = n.ref 
    def insert_empty( self , data ):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node 
        else: 
            print("the list is not empty")
                
    def add_begin(self, data):
        new_node = Node(data ) 
        new_node.ref = self.head  
        self.head = new_node 

    
    def add_end( self, data ):
        new_node = Node(data)
        
        if self.head is None: 
            self.head = new_node
        else:
            n = self.head 
            while n.ref is not None: 
                n = n.ref
            
            n.ref = new_node
            
            
    def add_after_node( self, data , value ):
        n = self.head 
        
        while n is not None:
            if n.data == value:
                break 
            n = n.ref 
        
        if n is None:
            print('No node found')
        else: 
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node
            
            
    def add_before_node( self , data , value ):
        if self.head is None :
            print("its empty cannot add")
            return
        
        if self.head.data == value: 
            new_node = Node(data ) 
            new_node.ref = self.head  
            self.head = new_node 
            return
         
        n = self.head 
            
        while n.ref is not None:
            if n.ref.data == value :
                break 
            n = n.ref 
        
        if n.ref is None:
            print("Non was found ")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node
                
        
        
        
                
        

ll = LinkedList()
ll.add_end(3)
ll.add_after_node(4 ,23)
ll.add_before_node(5 ,4)

ll.print_ll()