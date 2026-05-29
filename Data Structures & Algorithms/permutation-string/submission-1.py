class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        x=sorted(s1)
        f=False
        for i in range((len(s2))-(n-1)):
            y=sorted(s2[i:i+n])
            if x==y:
                f=True

            
        return f


        