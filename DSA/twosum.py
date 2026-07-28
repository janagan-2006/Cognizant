class twosum:
    def twosum_solution(self, target,a):
        # for i in range(len(a)):
        #     for j in range(len(a)-1):
        #         if a[i]+a[j]==target:
        #             return a[i],a[j]
        dict={}
        for i in range(len(a)):
            if a[i] in dict.keys():
                print(dict.keys())
                return dict.get(a[i]),a[i]
            dict[target-a[i]]=a[i]
s1=twosum()
print(s1.twosum_solution(9,[4,3,6,5]))