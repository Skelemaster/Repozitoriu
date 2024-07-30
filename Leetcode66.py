class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        List1=[]
        G=""
        for i in digits:
            G+=f"{i}"
        G=str(int(G)+1)
        for i in G:
            List1.append(int(i))
        return List1



obj = Solution()
print(obj.plusOne(digits=[4,3,2,1]))