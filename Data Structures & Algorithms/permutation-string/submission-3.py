class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if len(s2)<len(s1):
        return False
      
      sMap={}
      for c in s1:
        sMap[c]=sMap.get(c,0)+1
      
      for i,t in enumerate(s2):
        if t in s1:
          maxIndex=min(i+len(s1),len(s2))
          tempMap={}
          for idx in range(i,maxIndex):
            tempMap[s2[idx]]=tempMap.get(s2[idx],0)+1
          print(tempMap)
          if tempMap==sMap:
            return True
          
      return False