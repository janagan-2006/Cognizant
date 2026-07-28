class Solution(object):
    def removeOuterParentheses(self, s):
        answer=""
        process=[]
        for c in s:
            if(c=='('):
                if process:
                    answer+=c
                process.append(c)
            if(c==')'):
                if len(process)>1:
                    answer+=c
                process.pop()
        return answer
s1=Solution()
print(s1.removeOuterParentheses("(()())((()))"))