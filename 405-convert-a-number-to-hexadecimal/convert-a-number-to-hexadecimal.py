class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        binary = ""
        for i in range(31, -1, -1):
            binary += str((num >> i) & 1)
        groups = []
        for i in range(0, 32, 4):
            group = binary[i:i+4]
            groups.append(group)
        hex_map = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "a", "1011": "b",
            "1100": "c", "1101": "d", "1110": "e", "1111": "f"
        }
        result = ""
        for group in groups:
            result += hex_map[group]

        result = result.lstrip("0")

        if not result:
            return "0"
        
        return result
        