# Variables enabling execution time
execution_time = input("Enter execution time in minutes: ")
# Type conversion
minutes = int(execution_time)
# Arithmetic: Float Division
hours = minutes / 60

# Execution time output
print(f"Minutes: {minutes}")
# f-strings & 2 decimal places
print(f"Hours: {hours:.2f}")
# Version below without 2 decimals
# print(f"Hours: {hours:}")