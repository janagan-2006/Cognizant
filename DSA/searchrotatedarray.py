class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            if(mid==target):
                return target
            elif low>target:
                low=mid+1
            elif high<target:
                high=mid-1
        return mid
