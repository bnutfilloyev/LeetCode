class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp = []
        
        for i, v in enumerate(s):
            if v == c:
                temp.append(i)
                
        
        res = []
        
        for i in range(len(s)):
            res.append(min([abs(i - j) for j in temp]))
        
        return res