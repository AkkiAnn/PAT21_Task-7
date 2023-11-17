# Import datetime 
import datetime
# Function that creates a text file with current timestamp
def create_timestamp_file():
# Get current datetime 
    now = datetime.datetime.now()
# Datetime object as a string
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
 # Create a file name with timestamp
    file_name = timestamp + ".txt"
# Open file in write mode
    file = open(file_name, "w")
# Write timestamp to file
    file.write(timestamp)
# Close  file
    file.close()
 # Return file name
    return file_name
# Call function and print result
result = create_timestamp_file()
print("The file name is:", result)
