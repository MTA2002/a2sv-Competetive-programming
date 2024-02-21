class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_length = len(nums1)
        ans = [-1] * nums1_length
        stack = []
        valid = {}
        for i in range(nums1_length):
            valid[nums1[i]] = i
            
        for j in range(len(nums2)):
            while stack and stack[-1] < nums2[j]:
                popped = stack.pop()
                if popped in valid:
                    ans[valid[popped]] = nums2[j]
                    
            stack.append(nums2[j])

        return ans
