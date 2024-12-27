def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example usage:
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, "hello"))