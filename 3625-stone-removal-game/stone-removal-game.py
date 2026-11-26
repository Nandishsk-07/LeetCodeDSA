class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stones_to_remove = 10
        alice_turn = True
        while n >= stones_to_remove and stones_to_remove > 0:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
        return not alice_turn
    
        