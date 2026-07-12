class Node:
    def __init__(self,key,val):
        self.key = key
        self.val= val
        self.prev = None
        self.next = None

#helper functions

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.m = {} #creating a map to keep the track of nodes

    #helper functions
    def addNode(self,newnode):
        temp=self.head.next
        newnode.next=temp
        newnode.prev = self.head
        self.head.next =newnode
        temp.prev=newnode
    
    def deleteNode(self,newNode):
        prevNode = newNode.prev
        NextNode = newNode.next

        prevNode.next = NextNode
        NextNode.prev = prevNode
    

    def get(self, key: int) -> int:

        if key  in self.m:
            node = self.m[key]
            value = node.val
            del self.m[key]
            
            self.deleteNode(node)
            self.addNode(node)
            
            self.m[key]=self.head.next #initlizing the first node
            return value
        return -1
        
        

    def put(self, key: int, value: int) -> None: #if already exist we need to delete and add back
        if key in self.m:
            existingNode = self.m[key]
            del self.m[key]
            self.deleteNode(existingNode)

        if len(self.m)==self.cap:
            self.m.pop(self.tail.prev.key) #removign from the map
            self.deleteNode(self.tail.prev)
        
        self.addNode(Node(key,value)) #while adding Node we need to handle Node(Key,value)
        self.m[key] = self.head.next #reassigning teh value to the map
        
