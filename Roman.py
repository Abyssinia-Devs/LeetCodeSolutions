class Solution(object):
    def romanToInt(self, s):
        self.s = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0

        for i in range(len(s)):
            # if next symbol exists AND current < next → subtract
            if i + 1 < len(s) and self.s[s[i]] < self.s[s[i + 1]]:
                total -= self.s[s[i]]
            else:
                total += self.s[s[i]]

        return (total)
        
runn = Solution()
runn.romanToInt('III')
runn.romanToInt('LVIII')
runn.romanToInt('MCMXCIV')