class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for path in paths:
            destination = path[1]
            i = 0

            for path2 in paths:
                if path[1] == path2[0]:
                    break
                i += 1

            if i == len(paths):
                return destination
