class Solution:
    def intToRoman(self, num: int) -> str:
        key=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        value=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        strng = ""
        while num>0:
            if num>=key[i]:
                strng+=value[i]
                num-=key[i]
            else:
                i+=1
        return strng
