class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        # h[key]=[]

        for word in strs:
            key = "".join(sorted(word))
            if key not in h:
                h[key]=[]
                h[key].append(word)
            else:
                h[key].append(word)
        return list(h.values())