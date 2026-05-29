class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=[]
        m=0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
            else:
                m=max(m,len(seen))
                while s[i] in seen:
                    del seen[0]
                seen.append(s[i])
                

        m=max(m,len(seen))  
        return m

        