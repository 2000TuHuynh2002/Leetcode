class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_dict = {}
        consonant_dict = {}

        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u']:
                try:
                    vowel_dict[c] += 1
                except:
                    vowel_dict[c] = 1
            else:
                try:
                    consonant_dict[c] += 1
                except:
                    consonant_dict[c] = 1

        return max(vowel_dict.values(), default=0) + max(consonant_dict.values(), default=0)
