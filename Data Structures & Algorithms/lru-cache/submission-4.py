class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:
    def remove(self,node):
        nex=node.next
        pre=node.prev
        pre.next=nex
        nex.prev=pre
        node.prev=None
        node.next=None

    def insert(self,node):
        pre=self.tail.prev
        pre.next=node
        node.next=self.tail
        node.prev=pre
        self.tail.prev=node

    def __init__(self, capacity: int):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.maxcapacity=capacity
        self.cache={}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            node.value=value
            self.insert(node)
            return
        node=Node(key,value)
        if len(self.cache)==self.maxcapacity:
            new=self.head.next
            del self.cache[new.key]
            self.remove(new)

        self.insert(node)
        self.cache[key]=node

