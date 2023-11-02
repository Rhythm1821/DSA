class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:return True
        if n%2==1:return False
        return self.recursion(1,n)
        
    def recursion(self,pow,n):
        if 2**pow==n:
            return True
        elif 2**pow<n:
            self.recursion(pow+1,n)
        else:
            return False