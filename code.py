class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
find the len ==> O(n)
        """
        if ( needle == "" or needle==haystack):
            return 0
        
        h_len = len(haystack)
        n_len = len(needle)
        
        start = 0
        
        while n_len+start <= h_len:
            if needle == haystack[start:start+n_len]:
                return start
            start += 1;
        return -1;