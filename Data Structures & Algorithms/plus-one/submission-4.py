class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits or digits is None:
            return 0
        carry,i=1,0
        digits=digits[::-1]
        while carry:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                    carry=1
                else:
                    carry=0
                    digits[i]+=1
            else:
                digits.append(1)
                carry=0
            i+=1
        return digits[::-1]
