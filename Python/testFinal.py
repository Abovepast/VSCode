def example():
    try:
        print("Inside try block")
        return 1
    finally:
        print("Inside finally block")

result = example()
print("Result:", result)
