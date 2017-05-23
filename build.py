def sum_two(a, b):
    if a is None or b is None:
        return False
    result = a ^ b;
    carry = (a & b) << 1
    if carry != 0:
        return sum_two(result, carry)
    return result;
