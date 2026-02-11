class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]  # start with the first word as the prefix
        
        for word in strs[1:]:
            # shrink the prefix until it matches the start of the word
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if prefix == "":
                    return ""  # no common prefix
        
        return prefix

# Example usage
runn = Solution()
print(runn.longestCommonPrefix(['flower','fly','fll']))
