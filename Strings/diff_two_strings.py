"""
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s
and then add one more letter at a random position.

Find the letter that was added in t.

"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp = dict()
        for k in s:
            if k in temp:
                temp[k] += 1
            else:
                temp[k] = 1
        for k in t:
            if k in temp:
                if temp[k] == 0:
                    return k
                else:
                    temp[k] -= 1
            else:
                return k
                
s = Solution()
print s.findTheDifference("qqwweerrttyyuuiioopp", "ppooiiuuyyttrreewwqqv")