class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        s_list = list(s)
        score = 0

        for i in range (1,n):
             score+= abs(ord(s_list[i])-ord(s_list[i-1]))
        
        return score 
        