# 📘 Assignment: Exception Handling in Python

## 🎯 Objective

Learn to handle errors gracefully in Python using try-except blocks. You'll write programs that catch exceptions, validate user input, handle file errors, and recover from common mistakes instead of crashing.

## 📝 Tasks

### 🛠️ Basic Try-Except Blocks

#### Description
Write a program that attempts risky operations and catches exceptions. Start with simple operations like type conversions and division, learning when and how exceptions occur and how to handle them with try-except blocks.

#### Requirements
Completed program should:

- Use try-except blocks to catch at least 3 different exception types (e.g., ValueError, ZeroDivisionError, TypeError)
- Demonstrate proper exception handling for user input conversion
- Display meaningful error messages to the user
- Continue program execution after handling an exception
- Show the difference between handled and unhandled exceptions

### 🛠️ File Handling with Exception Safety

#### Description
Create a program that reads from and writes to files, handling errors that might occur. Demonstrate safe file operations that don't crash if a file is missing or unreadable.

#### Requirements
Completed program should:

- Attempt to open and read a file with proper exception handling
- Handle FileNotFoundError when a file doesn't exist
- Use finally blocks to clean up resources (close files)
- Demonstrate both successful and failed file operations
- Provide helpful feedback when file operations fail

### 🛠️ Custom Validation with Multiple Exceptions

#### Description
Build a program that validates user input using multiple exception types. Create a system that checks for various invalid conditions and responds appropriately to each error type.

#### Requirements
Completed program should:

- Validate multiple input requirements (e.g., age must be positive integer, email format, etc.)
- Catch and handle different exceptions for different validation failures
- Re-prompt the user when validation fails
- Use custom error messages for each exception type
- Successfully accept and process valid input
