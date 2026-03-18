class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        j=0
      
        s=list(s)
        vowelsd=[]
        vowels = "aeiouAEIOU"
        for i in range (len(s)):
             if s[i] in vowels:
                vowelsd.append(s[i])
        vowelsd=vowelsd[::-1]
        
        
       
        for i in range(len(s)):
              if s[i] in vowels:
                    s[i]=vowelsd[j]
                    j+=1
        return "".join(s)
runn=Solution()
(runn.reverseVowels('ICEream'))
#s='hellomothere'
#print(s.index('h'))


"""for letter in s:
           # if letter in vowels:
               # s[s.index(letter)]= 'j'
                pass"""