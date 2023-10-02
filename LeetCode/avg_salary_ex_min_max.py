class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n = len(salary)
        total = float(sum(salary)) - (min(salary) + max(salary))
        return total/(n-2)