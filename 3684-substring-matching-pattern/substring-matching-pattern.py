class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        start, end = s.find(prefix), s.rfind(suffix)
        if start == -1 or end == -1:
            return False
        return start + len(prefix) <= end
