class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = []
        while n > 0:
           seen = []
           j = 0

           while n > 0:
             digit = n % 10
             seen.append(digit)
             n = n // 10

           for i in seen:
             j += i * i

           if j == 1:
             return True

           if j in k:   # cycle detected
             return False

           k.append(j)
           n = j
        
    

runn=Solution()
print(runn.isHappy(19))
print(runn.isHappy(2))
"""k=0
        while n > 0:
          seen = []
          j = 0
          
          while n > 0:
            digit = n % 10
            seen.append(digit)
            n = n // 10

          for i in seen:
             j += i * i
          
          if j > k:
             if j==1:
               return True
          else:
             return False

          n = j
          k=j"""