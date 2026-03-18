class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
       
        for i in range(len(digits) - 1, -1, -1):

          if digits[i] < 9:
            digits[i] += 1
            return digits  # stop immediately

          # if digit is 9
          digits[i] = 0  

   
        return [1] + digits   






"""class Solution(object):
    def plusOne(self, digits):
       
        :type digits: List[int]
        :rtype: List[int]
   
       
        for i in range (0,len(digits)):
           if i== len(digits)-1:
            if digits[i] <9:
                digits[i]=digits[i]+1
            elif digits [i]>=9:
                digits[-1:] = [int(x) for x in str(digits[-1] + 1)]
               
            return digits
runn=Solution()
print(runn.plusOne([1,3,10]))   
print(runn.plusOne([2,3,4,4,5]))   """ 

