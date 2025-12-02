class Solution(object):
    def removeElement(self, nums, val):
        temp = []
        for x in nums:
            if x != val:
                temp.append(x)

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)

