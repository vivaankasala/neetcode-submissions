class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        zero=nums.count(0)
        res=[]
        product=1
        for num in nums:
            if num==0:
                continue
            else:
                product*=num
        if zero>1:
                return [0] * len(nums)

        for num in nums:
            if num==0:
                res.append(int(product))
            elif zero==1:
                res.append(0)
            
            elif zero==0:
                res.append(int(product//num))
        return res