class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        result = ""

        for idx, s in enumerate(num_str):
            if num_str[idx] == "6":
                result += "9" + num_str[idx + 1:]
                return int(result)
            result += s

        return int(result)
