class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bit_a = (a>>i) & 1
            bit_b = (b>>i) & 1

            sum_bit = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))
            res |= (sum_bit<<i)
        
        res &= mask
        return res if res <= 0x7FFFFFFF else ~(res ^ mask)