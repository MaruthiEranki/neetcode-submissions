class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split(' ')
        s = ''.join(s).lower()
        start_index = 0
        end_index = len(s)-1
        while start_index < end_index:
            if not s[start_index].isalnum():
                start_index = start_index + 1
                continue
            if not s[end_index].isalnum():
                end_index = end_index - 1
                continue
            if s[start_index] != s[end_index]:
                return False
            start_index = start_index + 1
            end_index = end_index - 1
        return True
        