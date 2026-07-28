class Solution(object):
    def romanToInt(self, s):
        for c in s[::-1]:
            value=self.getvalue(c)
            answer=0
            prevalue=0
            if(prevalue<=value):
                answer+=value
                prevalue=value
            else:
                answer-=value

    def getvalue(self,c):
        dict={'v':5,'I':1,'X':10,'L':50 ,'C':100,'D':500,'M':1000}
        return dict.get(c,0)   