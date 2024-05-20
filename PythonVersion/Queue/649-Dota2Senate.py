from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiantActive, direActive = 0,0
        radiantBanned, direBanned = 0,0
        senatorsDeque = deque()

        #count active senators and fill up queue 
        for char in senate:
            if char == "R":
                senatorsDeque.append((char, True))
                radiantActive += 1
            else: # senator is dire
                senatorsDeque.append((char, True))
                direActive += 1

        while radiantActive > 0 and direActive >0: 
            currentSenator, isActive = senatorsDeque.popleft()
            if currentSenator == "R": 
                if radiantBanned >0 and isActive:
                    isActive = False
                    radiantBanned -= 1
                elif isActive:
                    direBanned += 1
                    direActive -= 1
            else: # dire senator 
                if direBanned >0 and isActive:
                    isActive = False
                    direBanned -= 1
                elif isActive:
                    radiantBanned += 1
                    radiantActive -= 1
            senatorsDeque.append((currentSenator, isActive))
        return "Radiant" if radiantActive > 0 else "Dire"
