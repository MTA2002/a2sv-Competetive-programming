class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:

        if self.isFull() == False:
            self.rear += 1
            self.queue[(self.rear) % self.size] = value
            return True
        
        
        return False
        

    def deQueue(self) -> bool:
        if self.isEmpty() == False:
            self.front += 1
            self.queue[(self.front) % self.size] = -1
            
            return True
        
        return False

    def Front(self) -> int:
        if self.isEmpty() == False:
            return self.queue[(self.front+1) % self.size]
        
        return -1

    def Rear(self) -> int:
        if self.isEmpty() == False:
            return self.queue[(self.rear) % self.size]
        
        return -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front % self.size] == -1
        

    def isFull(self) -> bool:
        return self.queue[(self.rear + 1) % self.size] != -1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()