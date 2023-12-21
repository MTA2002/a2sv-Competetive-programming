class Robot:

    def __init__(self, width: int, height: int):
        self.direction = "East"
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        total = self.width * 2 + ( self.height - 2 ) * 2
        num = num % total
        if num == 0 and (self.x,self.y) == (0,0):
            self.direction = "South"
        while num > 0:
            if self.direction == "East":
                if num + self.x >= self.width:
                    inc=self.width - self. x -1
                    self.x += inc
                    num -= inc
                    self.direction = "North"
                else:
                    self.x += num
                    break
            if self.direction == "North":
                if num + self.y >= self.height:
                    
                    inc=self.height - self.y -1
                    self.y += inc
                    num -= inc
                    self.direction = "West"
                else:
                    self.y += num 
                    break
            if self.direction == "West":
                if  self.x - num < 0:
                    num -= self.x
                    self.x=0
                    self.direction = "South"
                else:
                    self.x -= num
                    break
            if self.direction == "South":
                if  self.y - num < 0:
                    num -= self.y
                    self.y=0
                    self.direction = "East"
                else:
                    self.y -= num
                    break
        
    def getPos(self) -> List[int]:
        return [self.x,self.y]
        

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()