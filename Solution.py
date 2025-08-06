class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s: return 0

        i = 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, num))
