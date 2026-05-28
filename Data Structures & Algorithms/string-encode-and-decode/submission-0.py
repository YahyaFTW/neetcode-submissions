class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded=encoded+ str(len(word))+"#"+word
        return encoded
        # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        decoded =[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j=j+1
            length = int(s[i:j])
            decoded.append(s[j+1:j+length+1])

            i=j+length+1
        return decoded

                


