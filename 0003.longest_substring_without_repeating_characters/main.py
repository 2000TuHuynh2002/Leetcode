class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        result_max = 0
        max_lenght = len(set(s))

        for char in s:
            if char in temp:
                position = temp.index(char)
                temp = temp[position + 1:]

            # Always append the current character to the temporary list.
            temp.append(char)

            # Update the maximum length if the current substring is longer than
            # the previous maximum length.
            if len(temp) > result_max:
                result_max = len(temp)

            # End the process early if the maximum length is reached. This is a
            # small optimization to avoid unnecessary iterations.
            if len(temp) == max_lenght:
                return max_lenght

        return result_max
