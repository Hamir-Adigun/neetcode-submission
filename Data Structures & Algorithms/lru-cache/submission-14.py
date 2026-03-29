class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.liste=[]
    def get(self, key: int) -> int:
        if key in self.dic:
            i=0
            while i <len(self.liste):
                if self.liste and self.liste[i]==key:
                    self.liste.pop(i)
                i+=1
            self.liste.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key]=value
        elif self.capacity==0:
            self.dic[key]=value
            k=self.liste.pop(0)
            self.dic.pop(k)
        else:
            self.dic[key]=value
            self.capacity-=1
        i=0
        while i <len(self.liste):
            if self.liste and self.liste[i]==key:
                self.liste.pop(i)
            i+=1
        self.liste.append(key)
            
        
