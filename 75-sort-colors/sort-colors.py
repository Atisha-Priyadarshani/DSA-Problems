class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0=p1=0
        for i in range(len(nums)):
            v=nums[i]
            nums[i]=2
            if v<2:
                nums[p1]=1
                p1+=1
                if v==0:
                    nums[p0]=0
                    p0+=1
        