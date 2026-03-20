class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        n=bin(n)
        n=n[2:]
        n=n[::-1]
        #print(n)
        indexes=[]
        even=[]
        odd=[]
        even_odd=[]

        for indexe,bit in enumerate (n):
            #print(bit)
            if bit=='1':
                indexes.append(indexe)
        #print(indexes)
        for  index1 in indexes:
            if (index1) %2==0:
                even.append(index1)
            elif index1 %2 !=0:
                odd.append(index1)
            
        #print(odd)
        
        even_odd.append(len(even))
        even_odd.append(len(odd))
        #print(even_odd)
        
        return even_odd

            

runn=Solution()
nnn=runn.evenOddBit(50)
print(nnn)