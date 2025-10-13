class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        word_map = {}

        if len(set(pattern)) != len(set(s_arr)):
            return False

        if len(pattern) != len(s_arr):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in word_map:
                word_map[pattern[i]] = s_arr[i]
                continue

            if word_map[pattern[i]] != s_arr[i]:
                return False

        return True
