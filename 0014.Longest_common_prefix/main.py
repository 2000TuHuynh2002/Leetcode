class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_prefix = ""
        idx = 0
        current_char = ""
        try:
            while(1):
                current_char = strs[0][idx]
                for single_str in strs:
                    if single_str[idx] != current_char:
                        return result_prefix
                idx += 1
                result_prefix += current_char
        except Exception as e:
            print(e)
            return result_prefix

