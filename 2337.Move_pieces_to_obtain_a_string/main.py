class Solution:
    def __get_indices(self, s, char):
        return [idx for idx, c in enumerate(s) if c == char]

    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True

        if start.replace("_", "") != target.replace("_", ""):
            return False

        start_L_indices = self.__get_indices(start, "L")
        start_R_indices = self.__get_indices(start, "R")
        target_L_indices = self.__get_indices(target, "L")
        target_R_indices = self.__get_indices(target, "R")

        for start_L_idx, target_L_idx in zip(start_L_indices, target_L_indices):
            if start_L_idx < target_L_idx:
                return False

        for start_R_idx, target_R_idx in zip(start_R_indices, target_R_indices):
            if start_R_idx > target_R_idx:
                return False

        return True
