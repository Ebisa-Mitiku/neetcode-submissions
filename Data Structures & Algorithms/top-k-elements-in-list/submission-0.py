class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        col=[]
        t=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        s=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for i in s:
            col.append(i)
        for i in range(k):
            t.append(col[i])
        return t
