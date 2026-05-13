class Solution:

    def encode(self, strs: List[str]) -> str:
        result: str = ""
        for s in strs:
            result += s + "§"
        return result
    def decode(self, s: str) -> List[str]:
        result: list = []
        word = ""
        for c in s:
            if c == "§":
                result.append(word)
                word = ""
            else:
                word += c
        return result