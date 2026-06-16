class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # Keep going until we hit 1 or start looping
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.next_gen(n)
            
        return n == 1
    def next_gen(self, number: int) -> int:
        total_sum=0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum 
       

        