class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for i,j in enumerate(nums):
            com=target-j
            if com in num:
                return[num[com],i]
            num[j]=i
        return None
        