# Exception Handling Starter Code
# Complete each task by filling in the TODO sections

# Task 1: Basic Try-Except Blocks
print("=" * 40)
print("Task 1: Basic Exception Handling")
print("=" * 40)

# TODO: Wrap the following code in try-except blocks to catch different exceptions
# 1. Try to convert user input to an integer
# 2. Try to convert user input to a float
# 3. Try to divide two numbers (watch for ZeroDivisionError)
# 4. Try to access a list index that doesn't exist

# Example structure:
# try:
#     # your risky code here
# except ValueError:
#     # handle ValueError
# except ZeroDivisionError:
#     # handle ZeroDivisionError
# except IndexError:
#     # handle IndexError


# Task 2: File Handling with Exception Safety
print("\n" + "=" * 40)
print("Task 2: File Handling")
print("=" * 40)

# TODO: Write a function that:
# 1. Attempts to open and read a file
# 2. Catches FileNotFoundError if file doesn't exist
# 3. Closes the file safely using finally or with statement

def read_file_safely(filename):
    """TODO: Complete this function"""
    # try:
    #     # Open and read the file
    #     # Process the content
    # except FileNotFoundError:
    #     # Handle missing file
    # finally:
    #     # Ensure file is closed


# Task 3: Custom Validation
print("\n" + "=" * 40)
print("Task 3: Input Validation")
print("=" * 40)

# TODO: Create a validation function that:
# 1. Accepts user input for multiple fields (e.g., age, email, username)
# 2. Validates each input and raises appropriate exceptions
# 3. Re-prompts the user if validation fails
# 4. Returns valid data when all validations pass

def validate_user_input():
    """TODO: Complete this function"""
    # while True:
    #     try:
    #         # Get input from user
    #         # Validate age (must be positive integer)
    #         # Validate email (must contain @)
    #         # Validate username (must be non-empty)
    #         # If all valid, return the data
    #     except ValueError:
    #         # Handle type conversion errors
    #     except Exception as e:
    #         # Handle custom validation errors


if __name__ == "__main__":
    # Test your code here
    pass
