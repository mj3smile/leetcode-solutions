class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n == 0 or n % groupSize > 0:
            return False
        
        freq = dict()
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        
        hand.sort()
        for h in hand:
            if h not in freq:
                continue
            
            size = 0
            target = h
            while target in freq and size < groupSize:
                freq[target] -= 1
                if freq[target] == 0: del freq[target]
                size += 1
                target += 1
            
            if size < groupSize:
                return False
        
        return len(freq) == 0