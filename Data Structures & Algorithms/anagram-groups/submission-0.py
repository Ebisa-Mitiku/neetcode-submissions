class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col=[]
        d=[]
        re=[]
        for i in range(len(strs)):
            if i not in re:
                d.append(strs[i])
            for j in range(i+1,len(strs)):
                if sorted(strs[i])==sorted(strs[j]) and i not in re:
                    d.append(strs[j])
                    re.append(j)
            if d:
                col.append(d)
            d=[]

        return(col)



        
                    

        