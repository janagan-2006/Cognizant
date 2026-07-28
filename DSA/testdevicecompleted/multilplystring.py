class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return "0"
        
        res=[0]*(len(num1)+len(num2))

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                mul=(ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                p1=i+j
                p2=i+j+1
                total_sum=mul+res[p2]

                res[p2]=total_sum%10
                res[p1]+=total_sum//10

        ans=[]
        for digit in res:
            if  (len(ans) != 0 or digit != 0):
                ans.append(str(digit))
                
        return "".join(ans)
    
s=Solution()
print(s.multiply("123", "45"))  # Output: "56088"

        