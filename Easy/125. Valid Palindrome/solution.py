class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''.join(i.lower() for i in s if i.isalnum())
        return all(k[i]==k[~i] for i in range(len(k)//2))
