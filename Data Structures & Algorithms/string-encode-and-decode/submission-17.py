class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # I thought that length is enough, however when its more than 2 digits you need a stopper "#"
            result += str(len(s)) + "#" + s
        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = 0
            while s[i + j] != "#":
                j += 1
            l = int(s[i : i + j])
            result.append(s[i + j + 1 : i + l + j + 1])
            i += l + j + 1
        return result

# Time: O(n), even though there are nested loops, the algorithm moves through each character individually
# Space: O(n), ever data structure is of length up to n