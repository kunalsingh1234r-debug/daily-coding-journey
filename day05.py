
filename = "coding_log.txt"

# 1. Writing data safely using a context manager ('with')
print("--- Writing to File ---")
try:
    with open(filename, "w") as file:
        file.write("Day 1: Setup and GitHub workflow\n")
        file.write("Day 2: Control flow and loops\n")
        file.write("Day 3: Functions and list statistics\n")
        file.write("Day 4: Dictionaries and frequency counting\n")
        file.write("Day 5: File I/O and exception handling\n")
    print(f"Successfully written logs to '{filename}'.")
except IOError as e:
    print(f"Error writing to file: {e}")

# 2. Reading file line-by-line and parsing records
print("\n--- Reading from File ---")
try:
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            print(f"Record {line_num}: {line.strip()}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")

# 3. Robust Exception Handling (ZeroDivision & Type conversions)
print("\n--- Exception Handling Demo ---")


def safe_metric_ratio(completed_tasks, total_tasks):
    try:
        ratio = completed_tasks / total_tasks
        return f"Completion Ratio: {ratio:.2%}"
    except ZeroDivisionError:
        return "Error: Total tasks cannot be zero."
    except TypeError:
        return "Error: Both task inputs must be numbers."


print(safe_metric_ratio(5, 5))
print(safe_metric_ratio(5, 0))
print(safe_metric_ratio("five", 5))