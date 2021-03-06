"""

174. Dungeon Game

The demons had captured the princess (P) and
imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health
(negative integers) upon entering these rooms; other rooms are either
empty (0's) or contain magic orbs that increase the knight's health
(positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health
so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight
must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

"""

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1
        
        for i in reversed(xrange(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
            for j in reversed(xrange(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j + 1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)
                
        return DP[0]
        
s = Solution()
print s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])