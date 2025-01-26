class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        k = nums   
        for num in k:
            if num == 0:
                count += 1
        while 0 in k:
            k.remove(0)
        for _ in range(count):
            k.append(0)
        return k