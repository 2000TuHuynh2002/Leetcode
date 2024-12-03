class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0

        for idx, char in enumerate(s):
            if space_idx < len(spaces) and idx == spaces[space_idx]:
                result.append(" ")
                space_idx += 1
            result.append(char)

        return "".join(result)
