class Solution:

    def encode(self, strs: List[str]) -> str:
        f=""
        for i in range(len(strs)):
            f=f+str(len(strs[i]))+"#"+strs[i]
        return f

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng=int(s[i:j])
            start=j+1
            end=start+leng
            res.append(s[start:end])
            i=end
        return res
        
        

