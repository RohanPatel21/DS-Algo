class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}
        for c1,c2 in zip(s,t):
            if (c1 not in mapST) & (c2 not in mapTS):
                mapST[c1] = c2
                mapTS[c2] = c1
            elif mapST.get(c1) != c2 or mapTS.get(c2) != c1:
                return False
        return True