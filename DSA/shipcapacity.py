class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=low+(high-low)//2
            day=1
            tempweight=0
            for weight in weights:
                if(tempweight+weight>mid):
                    day+=1
                    tempweight=0
                tempweight+=weight
            if(day>days):
                low=mid+1
            else:
                high=mid-1
        return mid       