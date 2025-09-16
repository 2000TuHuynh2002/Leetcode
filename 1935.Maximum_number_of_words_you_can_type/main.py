class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words_list = text.split(" ")
        count = len(words_list)

        for word in words_list:
            for letter in brokenLetters:
                if letter in word:
                    count -= 1
                    break

        return count
