class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        day_money = 0

        for i in range(1, n + 1):
            c = i % 7
            if c == 0:
                count += day_money + 7
            else:
                count += day_money + c

            if c == 0:
                day_money += 1

        return count
