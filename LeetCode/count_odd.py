class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        diff = high - low + 1
        if diff %2 == 0:
            return diff/2
        else:
            if low %2 == 0:
                return diff//2
            else:
                return diff//2 + 1