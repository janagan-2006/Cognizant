class zigzag:
    def zigzag_answer(self,s,n)->str:
        if len(s)<=n or n<=1:
            return s
        rows=["" for i in range(n)]
        currrow=0
        goingdown=False
        for char in s:
            rows[currrow]+=char
            if(currrow==0 or currrow==n-1):
                goingdown=not goingdown
            currrow=currrow+1 if goingdown else currrow-1
        return "".join(rows)
        print(rows)
if __name__=="__main__":
    solution=zigzag()
    result=solution.zigzag_answer("PAYPALISHIRING", 3)
    print(result)