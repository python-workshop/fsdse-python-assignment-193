def build(a, b):
    if a is None or b is None:
        return False
    result = a ^ b;
    carry = (a & b) << 1
    if carry != 0:
        return build(result, carry)
    return result;
result11 = build(3,2)
print (result11)