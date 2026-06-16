class Solution:
    def isHappy(self, n: int) -> bool:

        def next_gen(number):
            total_sum=0
            while number > 0:
                digit = number % 10
                total_sum += digit ** 2
                number //= 10
            return total_sum
        slow=n
        fast=next_gen(n)

        while fast!=1 and slow!=fast:
            slow=next_gen(slow)
            fast=next_gen(next_gen(fast))
        return fast==1
        