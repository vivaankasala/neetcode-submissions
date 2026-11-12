class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)
        for num in numSet:
            curr=num
            if(num-1) not in numSet:
                length=1
                while curr+1 in numSet:
                    length+=1
                    curr+=1
                longest=max(length,longest)
                

        return longest