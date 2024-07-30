class Solution:
    def Max(self, nums: list[int]) -> int: 
        max_value=nums[0]
        for k in nums:
            if max_value<k:
                max_value=k
        return max_value    
    def Min(self, nums: list[int]) -> int:
        min_value=nums[0]
        for k in nums:
            if min_value>k:
                min_value=k
        return min_value    
    def maxProductDifference(self, nums: list[int]) -> int:
        List1=[]
        List2=[]
        G=self.Max(nums)
        List1.append(G)
        nums.remove(G)
        G=self.Max(nums)
        List1.append(G)
        nums.remove(G)
        G=self.Min(nums)
        List2.append(G)
        nums.remove(G)
        G=self.Min(nums)
        List2.append(G)
        nums.remove(G)
        return ((List1[0]*List1[1])-(List2[0]*List2[1]))
        
        

obj = Solution()
print(obj.maxProductDifference(nums=[1,2,3,4,5,6]))