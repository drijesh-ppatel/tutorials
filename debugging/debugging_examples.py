def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Example issue: Accessing non-existent dictionary keys
my_dict = {"name": "AI Tool"}

try:
    value = my_dict["age"]
except KeyError:
    print("KeyError: 'age' does not exist.")

# Fix using dict.get()
age = my_dict.get("age", "Key not found")
print(age)
