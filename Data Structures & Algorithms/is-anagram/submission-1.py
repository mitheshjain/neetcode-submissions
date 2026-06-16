class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for c in s:
            if c in t:
                new_text = t.replace(c, "", 1)
                t=new_text
            else:
                return False
        if not t:
            return True
        return False