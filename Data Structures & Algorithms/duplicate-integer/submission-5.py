class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alpha_dict = {}
        for eachNum in nums:
            print(eachNum)
            if eachNum in alpha_dict:
                return True
            alpha_dict[eachNum] = 1
        return False