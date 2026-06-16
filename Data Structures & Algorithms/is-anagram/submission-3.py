class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)!=len(t):
        return False
      freq={}
      occur={}
      for c in s:
        freq[c]=1+freq.get(c,0)
    
      for h in t:
         occur[h]=occur.get(h,0)+1
      
      if freq!=occur:
        return False
      return True
