class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        moves_zero=0
        for i in range(n):
            if nums[i]!=0:
                nums[moves_zero]=nums[i]
                moves_zero += 1
        for i in range(moves_zero,n):
            nums[i]=0     
        