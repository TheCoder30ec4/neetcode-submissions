class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(clean_s)

        i,j = 0,len(clean_s)-1

        while i<j:

            if clean_s[i] == clean_s[j]:
                i+=1
                j-=1
                continue
            else:
                return False

        return True

        