class Solution:
    def twoSum(self, nums: List[int],target):
        dict={}

        for index,value in enumerate(nums):
            if (target - value) not in dict:
                dict[value] = index
            else:
                return [dict[target - value],index]