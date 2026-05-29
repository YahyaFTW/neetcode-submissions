class Solution:
# strs = ["Hello","World"]
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            length = str(len(word))
            encoded += length + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j=j+1
            length=int(s[i:j])
            decoded.append(s[j+1:j+length+1])
            i=j+1+length
        return decoded











