# Import the struct module
import struct
import os

# Define the path to the input folder
input_folder = f"C:\\Users\\{os.environ['USERNAME']}\\Documents\\Image-Line\\FL Studio\\Presets\\Plugin database\\Installed\\Effects\\New"

# Define the path to the output folder
output_folder = f"C:\\Users\\{os.environ['USERNAME']}\\Documents\\Image-Line\\FL Studio\\Presets\\Plugin database\\Effects\\USER"

# Define the file extension for the plugins
file_ext = ".fst"

# Define a function to read the vendor name from a binary file
def read_vendor_name(file_path):
    # Open the file in binary read mode
    with open(file_path, "rb") as f:
        # Read the whole file content
        data = f.read()
        # Find the index of the last 7 empty bytes (14 hex digits)
        index = data.rfind(b"\x00" * 7)
        # Extract the vendor name as a string after the empty bytes
        vendor_name = data[index + 7:].decode()
        # Return the vendor name
        return vendor_name

# Define a function to copy a file to a new folder named after the vendor
def copy_to_vendor_folder(file_path, vendor_name):
    # Import the os and shutil modules
    import os
    import shutil
    # Get the file name from the file path
    file_name = os.path.basename(file_path)
    # Create a new folder path with the output folder and the vendor name
    new_folder = os.path.join(output_folder, vendor_name)
    # Create the new folder if it does not exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    # Create a new file path with the new folder and the file name
    new_file = os.path.join(new_folder, file_name)
    # Copy the file to the new file path
    shutil.copy(file_path, new_file)

# Loop through all the files in the input folder
for file in os.listdir(input_folder):
    # Check if the file has the correct extension
    if file.endswith(file_ext):
        # Get the full file path by joining the input folder and the file name
        file_path = os.path.join(input_folder, file)
        # Read the vendor name from the file
        vendor_name = read_vendor_name(file_path)
        # Copy the file to a new folder named after the vendor
        copy_to_vendor_folder(file_path, vendor_name)
        # Copy also the .nfo file with the same name as the .fst file
        copy_to_vendor_folder(file_path.replace(".fst", ".nfo"), vendor_name)

# Print a message when done
print("All files copied successfully!")
