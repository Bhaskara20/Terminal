from os import getcwd


# Python program to explain shutil.copy() method

# importing shutil module
import shutil

# Source path
source = "andru.txt"

# Destination path
destination = "testing"

# Copy the content of
# source to destination

try:
	shutil.copy(source, destination)
	print("File copied successfully.")

# If source and destination are same
except shutil.SameFileError:
	print("Source and destination represents the same file.")

# If there is any permission issue
except PermissionError:
	print("Permission denied.")

# For other errors
except:
	print("Error occurred while copying file.")
