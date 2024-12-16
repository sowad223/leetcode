class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 0
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1

            dividend -= temp_divisor

            quotient += (1 << num_shifts)

        quotient = sign * quotient

        return max(INT_MIN, min(INT_MAX, quotient))
