class Solution:
    def answer(self, n):
        answer=[]
        x=[]
        for i in range(n):
            x=[]
            for j in range(i+1):
                if j==0 or j==i:
                    x.append(1)
                else:
                    x.append(answer[i-1][j-1]+answer[i-1][j])
            
            answer.append(x.copy())
            # x.clear()
            print(answer)
        return answer           

s = Solution()

print(s.answer(5))   # True
        # True

