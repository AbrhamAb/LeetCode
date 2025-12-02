class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set()
        for x in nums1:
            for y in nums2:
                if x == y:
                    seen.add(x)
        return list(seen)
