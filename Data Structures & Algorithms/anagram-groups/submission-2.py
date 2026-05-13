class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            frequency = [0] * 26 # each index is a letter in the alphabet, there are 26 of them
            for c in s:
                """
                ord gives a numeric value of a char, ord('a')=97, ord('b')=98, and so on
                ord('a')-ord('a')=0 as an index of 'a' suppose to be in the frequency array
                ord('b')-ord('a')=1 as an index of 'b' suppose to be in the frequency array
                """
                index = ord(c) - ord('a') # finds an appropriate index for letter c
                frequency[index] += 1
            key = tuple(frequency) # covert list into hashable value that can be a key for a dict
            if key not in result:
                result[key] = [s]
            else:
                result[key].append(s)
        return list(result.values())