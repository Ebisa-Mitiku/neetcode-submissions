class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t=nums.count(0)
        mul=1
        for i in range(len(nums)):
            mul*=nums[i]
        k=1
        for i in range(len(nums)):
            if nums[i]!=0:
                k*=nums[i]

        if t>=2:
            return [0]*len(nums)
        if t==1:
            f=[]
            for i in range(len(nums)):
                if nums[i]!=0:
                    f.append(0)
                else:
                    f.append(k)
            return f
                

        f=[]
        for i in range(len(nums)):
            x=mul//nums[i]
            f.append(x)
        return f


        