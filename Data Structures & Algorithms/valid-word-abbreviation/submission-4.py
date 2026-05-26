class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        if word == abbr:
            return True 

        
        i,j = 0,0

        while i<len(word) and j<len(abbr):

            if abbr[j].isdigit():

                if abbr[j] == "0":
                    return False 


                nums = 0

                while j<len(abbr) and abbr[j].isdigit():
                    nums = nums*10 + int(abbr[j])
                    j+=1
                i+=nums
                continue

            elif word[i] != abbr[j]:
                return False 
            
            i+=1
            j+=1

        return i==len(word) and j==len(abbr)


           

