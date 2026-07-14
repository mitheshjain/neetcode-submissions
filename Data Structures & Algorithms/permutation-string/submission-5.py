class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        for c in s1:
            count1[ord(c)-ord('a')]+=1
        for i,c in enumerate(s2):
            if c in s1:
                print (i)
                count2=[0]*26
                for x in range(i,min(i+len(s1),len(s2))):
                    count2[ord(s2[x])-ord('a')]+=1
                print(count2)
                print(count1)
                if count1==count2:
                    return True
        return False