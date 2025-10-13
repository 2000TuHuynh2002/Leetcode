class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word_dict = {}

        for a, b in zip(s, t):
            if not (a in word_dict):
                word_dict[a] = b
                continue
            if word_dict[a] != b:
                return False

        if len(set(word_dict.keys())) != len(set(word_dict.values())):
            return False

        return True
