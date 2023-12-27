class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)

        res = []

        for num in nums1_count:
            if num in nums2_count:
                frequency = min(nums1_count[num],nums2_count[num])
                for i in range(frequency):
                    res.append(num)

        return res
