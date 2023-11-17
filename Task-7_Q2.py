# Define function that reads text file
def read_from_file(file_name):
# Open file in read mode
    file = open(file_name, "r")
 # Read content of file
    content = file.read()
# Close file
    file.close()
 # Display content of file
    print("The content of file is:", content)

