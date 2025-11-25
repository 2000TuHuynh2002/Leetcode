class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numBottlesConsumed = 0
        while numBottles >= numExchange:
            k = numBottles // numExchange
            numBottlesConsumed += numExchange * k
            numBottles -= numExchange * k
            numBottles += k
        return numBottlesConsumed + numBottles
