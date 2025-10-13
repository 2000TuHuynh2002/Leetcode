class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        list_char = []
        list_idx = []

        for idx, char in enumerate(s):
            if char in "aeiouAEIOU":
                list_char.append(char)
                list_idx.append(idx)
        
        for i in list_idx:
            s[i] = list_char.pop()
        
        return ''.join(s)