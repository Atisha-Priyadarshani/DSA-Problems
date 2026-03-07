class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos_indx=0
        neg_indx=1
        for num in nums:
            if num>0:
                ans[pos_indx]=num
                pos_indx += 2
            else:
                ans[neg_indx]=num
                neg_indx +=2
        return ans            
        