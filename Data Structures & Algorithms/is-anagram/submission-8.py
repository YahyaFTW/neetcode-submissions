class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        h = {}
        for ch in s:
            h[ch] = h.get(ch, 0)+1
        for ch in t:
            h[ch] = h.get(ch, 0)-1
        for i in h.values():
            if(i!=0):
                return False
        return True