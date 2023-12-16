class ATM:

    def __init__(self):
        self.banknote_dict={
            0:500,
            1:200,
            2:100,
            3:50,
            4:20
        }
        self.banknote_list=[0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx,banknote in enumerate(banknotesCount):
            self.banknote_list[idx]+=banknote

    def withdraw(self, amount: int) -> List[int]:
        original_amount=amount
        result=[0]*5
        for i in range(5):
            if amount//self.banknote_dict[i] <= self.banknote_list[4-i]:
                result[4-i]=amount//self.banknote_dict[i]
                amount=amount%self.banknote_dict[i]
            else:
                
                result[4-i]=self.banknote_list[4-i]
                amount-=self.banknote_list[4-i]*self.banknote_dict[i]
        sum=0
        for i in range(5):
            sum+=result[i]*self.banknote_dict[4-i]
       
        if sum!=original_amount:
            return [-1]
        for i in range(5):
            self.banknote_list[i]-=result[i]
        return result

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)