class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        # h2={}
        for ch in s:
            h1[ch] = h1.get(ch, 0)+1
        for ch in t:
            h1[ch] = h1.get(ch, 0)-1
        for val in h1.values():
            if val !=0:
                return False
        return True