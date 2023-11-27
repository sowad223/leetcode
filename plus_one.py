class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join(map(str, digits))
        k = int(x)
        m = k + 1
        j = str(m)
        result = [int(digit) for digit in j]
        return result