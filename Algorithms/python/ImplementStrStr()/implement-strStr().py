class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)
        if haystack == needle:
            return 0
        if len_n > len_h:
            return -1

        for i in range(0, len_h - len_n + 1):
            # print(haystack[i: i+len_n])
            if haystack[i: i + len_n] == needle:
                return i
        return -1