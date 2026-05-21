class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # h={}

        # for word in strs:
        #     key = "".join(sorted(word))
        #     if key not in h:
        #         h[key]=[]
        #         h[key].append(word)
        #     else:
        #         h[key].append(word)
        # return list(h.values())





        map ={}

        for word in strs:
            key = "".join(sorted(word))
            if key in map:
                map[key].append(word)
            else:
                map[key]=[]
                map[key].append(word)
        return list(map.values())


















