class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum(heights[i] != expected[i] for i in range(len(heights)))
