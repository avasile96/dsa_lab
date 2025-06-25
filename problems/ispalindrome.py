def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]