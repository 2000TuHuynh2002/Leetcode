class Solution:
    def isValid(self, s: str) -> bool:
        char_opening = ["(", "[", "{"]
        char_closing = [")", "]", "}"]
        opening = []

        for char in s:
            if char in char_opening:
                opening.append(char)

            if char in char_closing:
                try:
                    if char == ")" and opening[-1] == "(":
                        opening.pop()
                    elif char == "]" and opening[-1] == "[":
                        opening.pop()
                    elif char == "}" and opening[-1] == "{":
                        opening.pop()
                    else:
                        return False
                # Exception in case "len(opening) == 0"
                except:
                    return False

        if len(opening) == 0:
            return True
        else:
            return False
