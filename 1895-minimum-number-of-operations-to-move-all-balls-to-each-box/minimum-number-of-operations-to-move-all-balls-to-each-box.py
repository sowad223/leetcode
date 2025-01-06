from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Calculate operations moving from left to right
        moves = 0
        balls = 0
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        # Calculate operations moving from right to left
        moves = 0
        balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        return answer

        