class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_added=False
        postive_pointer=0
        negative_pointer=0
        size=len(nums)
        result=[]

        while postive_pointer<size or negative_pointer<size:
            if postive_pointer<size and negative_pointer<size:
                if positive_added:
                    if nums[negative_pointer]<0:
                        result.append(nums[negative_pointer])
                        positive_added=False
                    negative_pointer += 1
                else:
                    if nums[postive_pointer]>0:
                        result.append(nums[postive_pointer])
                        positive_added=True
                    postive_pointer += 1
            elif postive_pointer==size and negative_pointer<size:
                if nums[negative_pointer]<0:
                    result.append(nums[negative_pointer])
                negative_pointer += 1
            else:
                if nums[postive_pointer]>0:
                        result.append(nums[postive_pointer])
                postive_pointer += 1
        return result