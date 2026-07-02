class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        num = int(str(abs(x))[::-1]) * sign

        return num if -2**31 <= num <= 2**31 - 1 else 0
        