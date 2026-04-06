class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = collections.Counter(hand)

        for card in sorted(count.keys()):
            if count[card] > 0:
                needed = count[card]

                for i in range(card, card+groupSize):
                    count[i] -= needed

                    if count[i] < 0:
                        return False
        return True