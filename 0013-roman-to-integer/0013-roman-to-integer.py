class Solution:
    def romanToInt(self, s: str) -> int:
        n={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        prev_val=0
        for i in s:
            if i in n:
                curr_val=n[i]
                if prev_val<curr_val:
                    res+=curr_val-(2*prev_val)
                else:
                    res+=curr_val
            prev_val=curr_val
        return res