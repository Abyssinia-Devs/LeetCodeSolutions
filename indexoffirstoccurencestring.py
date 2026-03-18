class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str      
        :type needle: str       
        :rtype: int             
        """

        # Loop through haystack
        # We stop at: len(haystack) - len(needle) + 1
        # because after that, there wouldn't be enough characters left
        # to match the whole needle
        for i in range(len(haystack) - len(needle) + 1):

            # Take a slice of haystack starting at index i
            # The slice has the same length as needle
            # Then compare it with needle
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


runn = Solution()
print(runn.strStr('hello', 'll'))      
print(runn.strStr('leetcode', 'leetoc'))
