class Solution(object):
    """
        :type s: str
        :rtype: int
    """
    def firstUniqChar(self, s):
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1  # count each character once

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
'''class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=[]
        for i in s:
            if s.count(i)==1:
                seen.append(s.index(i))
        if len(seen)>0:
          return seen[0]
        else:
            return -1
  '''      