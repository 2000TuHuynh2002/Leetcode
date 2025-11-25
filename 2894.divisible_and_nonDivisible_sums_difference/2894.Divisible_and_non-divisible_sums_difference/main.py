class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div = []
        not_div = []

        for i in range(1, n + 1):
            if i % m == 0:
                div.append(i)
            else:
                not_div.append(i)

        return sum(not_div) - sum(div)
