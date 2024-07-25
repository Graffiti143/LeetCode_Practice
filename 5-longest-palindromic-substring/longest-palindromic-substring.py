class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_pal(s,left,right):
            right -= 1 #Since index of last value will be len()-1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        len_dict = {}
        for right in range(len(s),0,-1):
            for left in range(len(s) - right + 1):
                if  check_pal(s, left, left+right):
                    return s[left : left + right]

        
    
    

