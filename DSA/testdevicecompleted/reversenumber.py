def revernumber(num):
    answer=0
    while(num>0):
        digit=num%10
        answer=digit+answer*10
        num//=10
    return answer
print(revernumber(1234))