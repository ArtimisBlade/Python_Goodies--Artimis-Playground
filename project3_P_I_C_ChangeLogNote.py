import os

# Below are the variables enabling the change log
name = input("Enter your name: ")
system_name = input("Enter your system name: ")
change = input("Describe the change: ")

# Define the folder to store the change logs
log_folder = "change_logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Auto-numbering logic: Count existing files in the folder to determine the next number
existing_logs = [f for f in os.listdir(log_folder) if f.startswith("log_")]
next_number = len(existing_logs) + 1

# Create the file name with auto-numbering and system name detail
file_name = f"log_{next_number}_{system_name}.txt"
file_path = os.path.join(log_folder, file_name)

# Below is the Change Log output
log_content = f"""--- CHANGE LOG ---
User: {name}
System: {system_name}
Change: {change}
------------------
"""

# Print to console
print(log_content)

# Store the change log into the file
with open(file_path, "w") as file:
    file.write(log_content)

print(f"Change log saved to: {file_path}")