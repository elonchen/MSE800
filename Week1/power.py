def power(x, y):
    """
    Calculate x raised to the power y.
    Handles positive, negative, and fractional exponents.
    """
    if y == 0:
        return 1
    
    if y < 0:
        return 1 / power(x, -y)
    
    if isinstance(y, float):
        import math
        return math.exp(y * math.log(x))
    
    result = 1
    for _ in range(y):
        result *= x
    
    return result


if __name__ == "__main__":
    test_cases = [
        (2, 10),
        (3, 3),
        (5, 0),
        (2, -3),
        (2, 0.5),
        (10, 6),
    ]

    for x, y in test_cases:
        print(f"{x} ^ {y} = {power(x, y)}")