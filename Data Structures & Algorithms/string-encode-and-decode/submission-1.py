class Solution:

    def encode(self, strs: List[str]) -> str:
        val =""
        for word in strs:
            val+=str(len(word))
            val+='#'
            val+=word
        return val

    def decode(self, s: str) -> List[str]:
        result =[]
        i=0
        #step 1 run a loop to get letter to flow till end
        while i<len(s):
            nums=""
            #step 2 get a total number
            while s[i]!='#':
                nums += s[i]
                i+=1
            
            #step 3 covnerting a str to number
            word_len = int(nums)
            
            #step 4 skip the #
            i+=1 #as always we need to skip no need to compare direct getting

            letter =[]
            #step 5 its time take the word len and append each letter into the word
            while word_len>0:

                letter.append(s[i])
                i+=1
                word_len-=1
            #step 6 take the each letter =[a,b,c]->abc
            word=''.join(letter)
            result.append(word)
        
        return result
            

            
