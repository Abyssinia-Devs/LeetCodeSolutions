class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz=[]
        for i in range(1, n+1):
            if (not (i %3==0 ))and not ((i %5 ==0)):
                fizzbuzz.append(str(i))
            if (i %5==0 )and (i % 3==0):
                fizzbuzz.append("FizzBuzz")
            elif i %3 ==0:
                fizzbuzz.append('Fizz')
            elif i % 5==0:
                fizzbuzz.append("Buzz")
            
        return (fizzbuzz)
runn =Solution()
runn.fizzBuzz(3)
ee=runn.fizzBuzz(15)
print((ee))