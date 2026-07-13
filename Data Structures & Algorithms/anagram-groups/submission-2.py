class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for s in strs:

            temp=[0]*26
            for ch in s:
                temp[ord(ch)-ord('a')]+=1
            key=tuple(temp)
            hmap[key].append(s)
        res=[]
        for values in hmap.values():
            res.append(values)
        return res