class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count  = 0
        for i in details:
            age_with_seat = i[-4:]
            age = int(age_with_seat[:2])
            if age > 60:
                count+=1

        return count       