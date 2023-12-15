class Bitset:

    def __init__(self, size: int):
        self.bitmap_list=[0 for i in range(size)]
        self.size=size
        self.one_count=0
        self.flip_count=0

    def fix(self, idx: int) -> None:
        if self.bitmap_list[idx]==0 and self.flip_count%2==0: 
            self.one_count+=1
            self.bitmap_list[idx]=1
        if self.bitmap_list[idx]==1 and self.flip_count%2!=0: 
            self.one_count+=1
            self.bitmap_list[idx]=0
    def unfix(self, idx: int) -> None:
        if self.bitmap_list[idx]==0 and self.flip_count%2!=0: 
            self.one_count-=1
            self.bitmap_list[idx]=1
        if self.bitmap_list[idx]==1 and self.flip_count%2==0: 
            self.one_count-=1
            self.bitmap_list[idx]=0
    def flip(self) -> None:
        self.flip_count+=1
        self.one_count=self.size-self.one_count
        
    def all(self) -> bool:
        return self.one_count==self.size

    def one(self) -> bool:
        return self.one_count>0

    def count(self) -> int:
        
        return self.one_count

    def toString(self) -> str:
        
        res=[]
        if self.flip_count%2==0:
            for bitmap in self.bitmap_list:
                res.append(str(bitmap))
        else:
            for bitmap in self.bitmap_list:
                if bitmap==0:
                    res.append('1')
                else:
                    res.append('0')      
        return ''.join(res)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()