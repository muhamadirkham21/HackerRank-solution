class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_five = 0
        count_ten = 0
        count_twenty = 0

        out = True
        i = 0
        while i < len(bills):
            if bills[i] == 5:
                count_five += 1
            elif bills[i] == 10:
                count_ten += 1
                count_five -=1
            else:
                count_twenty += 1
                if count_ten != 0:
                    count_ten -= 1
                    count_five -= 1
                else:
                    count_five -= 3
            
            if count_five < 0 or count_ten < 0 or count_twenty < 0:
                out = False
                break
            i += 1
        return out

        