class Solution:
    def romanToInt(self, s: str) -> int:
        List1=[]
        for i in s:
            if i == "I":
                i = 1
            elif i == "V":
                i = 5
            elif i == "X":
                i = 10
            elif i == "L":
                i = 50
            elif i == "C":
                i = 100
            elif i == "D":
                i = 500
            if i == "M":
                i = 1000
            List1.append(i)
        for i in range(len(List1)):
            if i+1==len(List1):
                break
            if List1[i]<List1[i+1]:
                List1[i+1]=List1[i+1]-List1[i]
                List1[i]=0
        G=0
        for i in List1:
            G+=i
        return G



obj = Solution()
print(obj.romanToInt(s="MCMXCIV"))