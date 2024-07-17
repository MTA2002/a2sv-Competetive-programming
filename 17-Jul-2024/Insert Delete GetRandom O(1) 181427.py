# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
       self.randomized_list = []
       self.randomized_dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.randomized_dict:
            self.randomized_list.append(val)
            self.randomized_dict[val] = len(self.randomized_list) -1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_dict:
            size = len(self.randomized_list)
            idx = self.randomized_dict[val]
            last_element = self.randomized_list[size -1]
            self.randomized_list[idx] , self.randomized_list[size -1] =self.randomized_list[size -1] , self.randomized_list[idx]
            self.randomized_dict[last_element] = idx
            del self.randomized_dict[val]
            self.randomized_list.pop()
            return True
        return False

    def getRandom(self) -> int:
        random_index=random.random()*len(self.randomized_list)
        random_index=int(random_index)
        return self.randomized_list[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()