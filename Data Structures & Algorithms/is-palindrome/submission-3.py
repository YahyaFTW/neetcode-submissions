class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=[]
        
        for ch in s:
            if ch.isalnum():
                ch=ch.lower()
                new_s.append(ch)
        for i in range(len(new_s)//2):
            if(new_s[i]!=new_s[len(new_s)-i-1]):
                return False
        return True
            

            