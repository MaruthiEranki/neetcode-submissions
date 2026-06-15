class Solution:

    def char_count(self, p: str):
        char_dict = {}
        for each_char in p:
            if (each_char in char_dict):
                char_dict[each_char] = char_dict[each_char] + 1
            else:
                char_dict[each_char] = 1
        return char_dict

    def isAnagram(self, s: str, t: str) -> bool:
        return self.char_count(s) == self.char_count(t)

