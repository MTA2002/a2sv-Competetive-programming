class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        for i in range(len(self.urls)-1,self.current,-1):
            self.urls.pop(i)
        
        self.urls.append(url)
        self.current = len(self.urls) - 1
        
    def back(self, steps: int) -> str:

        self.current -= steps
        self.current = 0 if self.current < 0 else self.current
        return self.urls[self.current]
   
    def forward(self, steps: int) -> str:
        self.current += steps
        self.current = len(self.urls) - 1 if self.current >= len(self.urls) else self.current
        return self.urls[self.current]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)