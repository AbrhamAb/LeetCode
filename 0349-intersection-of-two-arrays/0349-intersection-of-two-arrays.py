class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = []

        for x in nums2:
            if x in set1 and x not in result:
                result.append(x)
        return result
