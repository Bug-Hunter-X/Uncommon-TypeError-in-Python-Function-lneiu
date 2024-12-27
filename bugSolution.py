def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid input type. Inputs must be numbers.")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage:
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, "hello"))
print(function_with_uncommon_error("hello",2))