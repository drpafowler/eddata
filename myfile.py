import os
import sys

def set_working_directory_to_file_location():
  """Sets the current working directory to the directory where the script is located."""

  try:
    # More robust way to get the script's directory
    if getattr(sys, 'frozen', False):  # Check if running as a frozen executable
      current_file_path = sys.executable
    else:
      current_file_path = __file__  # Use __file__ if not frozen

    current_file_path = os.path.abspath(current_file_path) # Get the absolute path
    current_dir = os.path.dirname(current_file_path)

    os.chdir(current_dir)

    print(f"Current working directory set to: {current_dir}")

  except Exception as e:
    print(f"An error occurred: {e}")

# Call the function to set the directory
set_working_directory_to_file_location()

# Example: Print the current working directory to verify
print(f"Current working directory (verified): {os.getcwd()}")