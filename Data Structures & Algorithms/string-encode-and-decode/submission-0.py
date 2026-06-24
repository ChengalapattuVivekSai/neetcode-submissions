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
        while i<len(s):
            nums=""
            while s[i]!='#':
                nums += s[i]
                i+=1

            word_len = int(nums)

            i+=1 #as always we need to skip no need to compare direct getting

            letter =[]
            while word_len>0:

                letter.append(s[i])
                i+=1
                word_len-=1
            
            word=''.join(letter)
            result.append(word)
        
        return result
            

            
