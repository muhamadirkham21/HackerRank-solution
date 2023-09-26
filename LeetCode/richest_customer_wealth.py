class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in accounts:
            total = 0
            for j in i:
                total += j
            if total > res:
                res = total
        return res

